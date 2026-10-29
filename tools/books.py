#!/usr/bin/env python3
"""Summarise a year's books and flag problems before they reach the CA.

Usage:  python3 tools/books.py years/2026-27

Reads years/<year>/sales-register.csv and years/<year>/books/*.csv, writes
years/<year>/books/summary.md, and prints the flags. Needs only Python 3.
See guide/13-keeping-books.md for the registers and the rules they follow.
"""
import csv
import datetime as dt
import os
import sys

HEADS = [
    "Internet and telecom", "Electricity", "Office rent or co-working",
    "Software, hosting and subscriptions", "Computer accessories and repairs",
    "Repairs and maintenance", "Office supplies and consumables", "Business travel",
    "Conveyance and fuel", "Vehicle insurance", "CA, legal and professional fees",
    "Bank and platform charges", "Client meals and promotion", "Salaries paid to helpers",
    "Interest on a business loan", "Other",
]
BLOCKS = {"computer": 40, "plant": 15, "furniture": 10}   # s. 33 rates, per cent
CASH_LIMIT = 10000          # s. 36(4): cash to one person in a day above this is disallowed
CAPITALISE_OVER = 10000     # a common CA line; agree yours and change it here


def money(s):
    s = (s or "").replace(",", "").strip()
    return float(s) if s else 0.0


def day(s):
    try:
        return dt.date.fromisoformat((s or "").strip())
    except ValueError:
        return None


def rows(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8-sig") as f:
        return [r for r in csv.DictReader(f) if any((v or "").strip() for v in r.values())
                and "example row" not in (r.get("notes") or "")]


def inr(x):
    """Indian digit grouping: 12,34,567."""
    neg, x = x < 0, round(abs(x))
    s = str(x)
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        s = ",".join(parts) + "," + tail
    return ("-" if neg else "") + "₹" + s


def main(year_dir):
    name = os.path.basename(os.path.normpath(year_dir))          # eg 2026-27
    start = dt.date(int(name[:4]), 4, 1)
    end = dt.date(int(name[:4]) + 1, 3, 31)
    full_rate_by = end - dt.timedelta(days=179)                     # used 180 days or more
    books = os.path.join(year_dir, "books")
    flags = []

    def flag(where, what):
        flags.append(f"{where}: {what}")

    # receipts
    receipts = 0.0
    for i, r in enumerate(rows(os.path.join(year_dir, "sales-register.csv")), 2):
        v = money(r.get("inr_value"))
        where = f"sales-register.csv line {i} ({r.get('invoice_no')})"
        if not v:
            flag(where, "no INR value yet")
        d = day(r.get("invoice_date"))
        if not d or not start <= d <= end:
            flag(where, f"invoice date {r.get('invoice_date')!r} is outside {name}")
        if r.get("credit_date") and not r.get("advice_file"):
            flag(where, "paid but no remittance advice on file")
        receipts += v

    # expenses
    by_head = {h: 0.0 for h in HEADS}
    for i, r in enumerate(rows(os.path.join(books, "expense-register.csv")), 2):
        where = f"expense-register.csv line {i} ({r.get('vendor')}, {r.get('date')})"
        amount, gst = money(r.get("amount_inr")), money(r.get("gst_inr"))
        d = day(r.get("date"))
        if not d or not start <= d <= end:
            flag(where, f"date {r.get('date')!r} is outside {name}")
        if (r.get("paid_by") or "").strip().lower() == "cash":
            flag(where, "paid in cash" + (f": above {inr(CASH_LIMIT)}, disallowed (s. 36(4))" if amount > CASH_LIMIT else ""))
        if not (r.get("document") or "").strip():
            flag(where, "no document")
        elif not os.path.exists(os.path.join(year_dir, r["document"])):
            flag(where, f"document not found: {r['document']}")
        if not (r.get("business_pct") or "").strip():
            flag(where, "no business share")
        if amount > CAPITALISE_OVER and r.get("head") in ("Computer accessories and repairs", "Office supplies and consumables", "Other"):
            flag(where, f"{inr(amount)} under {r['head']}: is it an asset?")
        if r.get("head") not in by_head:
            flag(where, f"head {r.get('head')!r} is not one of the heads in chapter 02; not counted")
            continue
        net = amount - (gst if (r.get("itc_claimed") or "").strip().lower() == "yes" else 0)
        by_head[r["head"]] += net * min(100.0, money(r.get("business_pct"))) / 100

    # depreciation
    opening = {b: 0.0 for b in BLOCKS}
    for r in rows(os.path.join(books, "opening-wdv.csv")):
        if r.get("block") in opening:
            opening[r["block"]] = money(r.get("opening_wdv_inr"))
    adds_full = {b: 0.0 for b in BLOCKS}
    adds_half = {b: 0.0 for b in BLOCKS}
    asset_lines = []
    for i, r in enumerate(rows(os.path.join(books, "fixed-assets.csv")), 2):
        where = f"fixed-assets.csv line {i} ({r.get('particulars')})"
        b = (r.get("block") or "").strip()
        if b not in BLOCKS:
            flag(where, f"block {b!r} is not computer, plant or furniture")
            continue
        used = day(r.get("put_to_use_date")) or day(r.get("purchase_date"))
        if not used or not start <= used <= end:
            flag(where, f"put to use {r.get('put_to_use_date') or r.get('purchase_date')!r} is outside {name}")
            continue
        if not (r.get("document") or "").strip():
            flag(where, "no invoice")
        if not (r.get("business_pct") or "").strip():
            flag(where, "no business share")
        cost = (money(r.get("cost_inr")) - money(r.get("gst_itc_claimed_inr"))) * min(100.0, money(r.get("business_pct"))) / 100
        half = used > full_rate_by
        (adds_half if half else adds_full)[b] += cost
        asset_lines.append((r.get("particulars"), b, used, cost, half))

    dep_rows, dep_total = [], 0.0
    for b, rate in BLOCKS.items():
        base = opening[b] + adds_full[b]
        dep = base * rate / 100 + adds_half[b] * rate / 200
        closing = opening[b] + adds_full[b] + adds_half[b] - dep
        dep_total += dep
        dep_rows.append((b, rate, opening[b], adds_full[b], adds_half[b], dep, closing))

    expenses = sum(by_head.values())
    profit = receipts - expenses - dep_total

    out = [f"# Books summary: tax year {name}", "",
           f"Generated by tools/books.py on {dt.date.today().isoformat()}. Figures at business share; "
           f"assets put to use after {full_rate_by.isoformat()} at half rate.", "",
           "## Profit", "", "| | ₹ |", "|---|---:|",
           f"| Receipts (sales register) | {inr(receipts)} |",
           f"| Expenses | {inr(-expenses)} |",
           f"| Depreciation | {inr(-dep_total)} |",
           f"| **Profit on the books route** | **{inr(profit)}** |",
           f"| Presumptive profit for comparison (50 %) | {inr(receipts / 2)} |", "",
           "## Expenses by head", "", "| Head | ₹ |", "|---|---:|"]
    out += [f"| {h} | {inr(v)} |" for h, v in by_head.items() if v]
    out += ["", "## Depreciation by block", "",
            "| Block | Rate | Opening WDV | Additions, full rate | Additions, half rate | Depreciation | Closing WDV |",
            "|---|---:|---:|---:|---:|---:|---:|"]
    out += [f"| {b} | {r} % | {inr(o)} | {inr(f)} | {inr(h)} | {inr(d)} | {inr(c)} |" for b, r, o, f, h, d, c in dep_rows]
    if asset_lines:
        out += ["", "## Assets added", "", "| Item | Block | Put to use | Cost at business share | Rate |", "|---|---|---|---:|---|"]
        out += [f"| {p} | {b} | {u.isoformat()} | {inr(c)} | {'half' if h else 'full'} |" for p, b, u, c, h in asset_lines]
    out += ["", "## Flags", ""] + ([f"- {x}" for x in flags] or ["None."]) + [""]
    os.makedirs(books, exist_ok=True)
    with open(os.path.join(books, "summary.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))

    print(f"{name}: receipts {inr(receipts)}, expenses {inr(expenses)}, depreciation {inr(dep_total)}, "
          f"books profit {inr(profit)} (presumptive {inr(receipts / 2)})")
    print(f"wrote {os.path.join(books, 'summary.md')}")
    for x in flags:
        print("FLAG", x)
    return 1 if flags else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
