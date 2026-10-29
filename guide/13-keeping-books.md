# Keeping books: if you choose actual profit over presumptive

On the presumptive scheme you keep evidence (invoices, bank statements,
remittance advices) but no books. Choose the books route, or cross ₹75
lakh, or declare less than 50 %, and you must keep **books of account**
(old s. 44AA, now s. 62; Rule 46 of the Income-tax Rules, 2026) for **7
tax years**, and above ₹50 lakh of receipts have them **audited** (s. 63,
report in Form 26 by 30 September). This chapter is the working method:
what to record, when, and what the CA needs at the end.

The registers live in `years/<year>/books/`, and `tools/books.py` turns
them into a profit and loss summary, a depreciation schedule and a list of
problems to fix before the CA sees them.

## The rules that keep books clean

Settle these in the first year, write them in `NOTES.md`, and keep them.

1. **One bank account and one card for the work.** Fees come in there;
   business costs go out from there; a fixed monthly transfer goes to your
   personal account. Mixed accounts are the biggest source of CA hours.
2. **Claim only what was paid by bank or card.** Pay nothing in cash. A
   cash payment over ₹10,000 to one person in a day is disallowed (s.
   36(4)); smaller ones are hard to prove. Never take or repay a loan of
   ₹20,000 or more in cash (ss. 185, 188), or receive ₹2 lakh or more in
   cash (s. 186).
3. **A document behind every claimed line.** An invoice or receipt,
   preferably in your name (and with your GSTIN if registered). Whether a
   cost is business or personal is decided by the document and what it
   bought, not by the shop's name.
4. **Business share in writing.** For anything shared with home life
   (broadband, electricity, a phone, a car) record the percentage and how
   you arrived at it, and use the same method every year.
5. **Assets are capitalised, not expensed.** Agree the line with your CA
   (a common one: over about ₹10,000, or a warranty longer than a year).
   Record the **date put to use**; if you do not track it separately, use
   the invoice date, consistently. Assets put to use after 3 October get
   half the rate in the first year.
6. **GST**: if you are not claiming input credit, book costs **including**
   GST; if you are, book them **without** it and keep the credit separate.
7. **Personal money is drawings.** PPF, insurance premiums, mutual funds,
   family expenses paid from the work account are not business costs;
   they are drawings, and the CA shows them in your capital account.
8. **Income basis.** Book income on the invoice date (simplest, and it
   matches GST), and convert a USD invoice by the method you chose
   (`01-income-tax.md`). Keep both every year.
9. **Year-end items.** Card dues on 31 March are a liability; an invoice
   raised but unpaid on 31 March is a debtor; the CA's fee for the year is
   provided for in that year and paid the next.
10. **Back up.** If the books are electronic, Rule 46 asks for a backup
    kept on a server located in India; keep a copy in an Indian cloud
    region or on your own drive in India as well as anywhere else. Ask your
    CA how strictly to read it.

## The registers

| File | One row per | Fill |
|---|---|---|
| `sales-register.csv` (year folder) | invoice issued | as you invoice; complete when the advice arrives |
| `books/expense-register.csv` | business expense | monthly, from the bank and card statements |
| `books/fixed-assets.csv` | asset bought for the work | when you buy it |
| `books/opening-wdv.csv` | depreciation block | once a year, from last year's signed depreciation schedule |
| `books/accounts.csv` | bank account, card, wallet or broker account in your name | once, then when anything opens or closes |
| `books/year-end.csv` | balance on 31 March | in the first week of April |

Expense heads (`head` column) must be one of the heads in
`02-presumptive-or-books.md`; the tool rejects others. Depreciation
blocks are `computer` (40 %), `plant` (15 %) and `furniture` (10 %).

## Every month (20 minutes)

1. Download the work account's and the card's statements.
2. For every debit that is a business cost, add a row to the expense
   register: date, vendor, invoice number, head, amount, GST, how paid,
   business share, and the file name of the invoice. Put the invoice in
   `05-expenses/`.
3. Anything that is an asset goes in the fixed-asset register instead.
4. Personal spends from the work account: leave them out of the
   registers (they are drawings); note large ones in `NOTES.md`.
5. Run `python3 tools/books.py years/2026-27` and fix what it flags.

## At year end, for the CA

Run the tool, fix every flag, and send the CA the audit pack in
`checklists/books-year-end.md`. If you are audited, the CA will also ask
the questions the audit report (Form 26) asks; the checklist lists them
so you can answer before they come up.

## What the tool does and does not do

`tools/books.py` needs only Python 3 (no packages). It reads the year's
registers, totals expenses by head at their business share, computes
depreciation block by block (opening written-down value, additions at full
or half rate, closing value), adds the profit from the sales register,
and writes `books/summary.md`. It flags cash payments, rows without a
document, unknown heads, dates outside the year, missing business shares,
costs above the capitalisation line booked as expenses, and invoices
without a remittance advice.

It does not produce a balance sheet, handle disposals of assets, or
replace the CA's computation. It gives the CA clean, totalled, evidenced
registers, which is most of what the CA's fee pays for.
