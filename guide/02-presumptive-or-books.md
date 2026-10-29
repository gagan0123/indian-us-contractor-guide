# Presumptive or books: choosing how your profit is counted

## The two routes side by side

| | Presumptive (old s. 44ADA, now s. 58) | Books (old s. 44AA, now s. 62) |
|---|---|---|
| Profit taxed | **50 % of gross receipts** (or more, if you choose) | receipts minus actual expenses and depreciation |
| Who can use it | resident individual in a specified profession; **information technology, engineering and technical consultancy** are named in s. 62(4) | anyone |
| Receipts limit | ₹50 lakh, or **₹75 lakh if cash receipts are 5 % or less** (bank and Deel payouts are not cash) | none |
| Books to keep | not required by the scheme (keep the evidence anyway: invoices, bank statements, remittance advices) | compulsory for a specified profession, kept for **7 years** (Rule 46 of the Income-tax Rules, 2026): cash book, ledger, copies of bills issued, original expense bills over ₹250 |
| Tax audit | none, even between ₹50 and 75 lakh, if you declare at least 50 % | required if receipts exceed **₹50 lakh** (s. 63), report in Form 26 by 30 September |
| Return form | ITR-4, or ITR-3 if you hold any foreign asset | ITR-3, with a profit and loss account and balance sheet |
| Return due date | 31 August | 31 August; 31 October if audited |
| Advance tax | whole amount by **15 March** | 15 / 45 / 75 / 100 % by June, September, December, March |
| Typical CA cost | low | higher; more again with an audit |
| Lock-in | none: you can switch each year (the five-year lock-in applies only to the business scheme, s. 58(6)) | none |

## When presumptive wins

Your real expenses are below **half** your receipts. For a remote software
contractor they almost always are: a laptop, internet, a share of home
electricity, some software and the CA's fee rarely come close to 50 %.
So presumptive usually gives **lower tax and far less work**.

## When books can win

- Real expenses are **above half** of receipts. Rare for a solo
  developer; possible if you pay a subcontractor or an assistant, rent an
  office, or buy expensive hardware every year.
- Receipts exceed **₹75 lakh**. Presumptive is closed to you; books and an
  audit are compulsory.
- You want to declare **less than 50 %**. You can, but then you must keep
  books and get them audited (s. 58(3)), so it is the books route in
  practice.

## A quick test

```
Expected receipts this year             R
Real expenses (incl. depreciation)      E
Presumptive profit                      0.5 × R
Books profit                            R - E

E < 0.5 R  and  R ≤ ₹75 lakh   →  presumptive
E > 0.5 R                       →  books (and audit if R > ₹50 lakh)
R > ₹75 lakh                    →  books, and audit
```

The calculator on the guide page runs this with the tax on both.

## Things that are easy to miss

- **The 50 % is of gross receipts**, the amount you invoiced or were
  credited, before Deel's fees or the exchange margin. Agree with your CA
  which figure counts as receipts.
- **Depreciation is deemed claimed** under presumptive: the written-down
  value of your laptop falls each year as if you had claimed it (s.
  58(5)), so you cannot save it up for a later books year.
- **GST is separate.** Choosing presumptive income tax has no effect on
  GST registration or returns (`03-gst.md`).
- **Records still matter.** Even on presumptive, keep invoices, the bank
  statement, Deel's withdrawal confirmations and the bank's remittance
  advices, so you can prove gross receipts and export status if asked.
- **The profession question.** Software development and consulting are
  normally treated as "information technology", "engineering" or
  "technical consultancy", which are specified professions. If a CA reads
  your work as a business instead, s. 58's professional route (50 %) is
  replaced by the business route (6 % or 8 % deemed profit on turnover,
  with a five-year lock-in). Settle this with the CA in the first year.
