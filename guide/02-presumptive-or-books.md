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

## What counts as an expense on the books route

Allowed if laid out wholly and exclusively for the profession, not
capital and not personal (old s. 37(1), now s. 34(1)). Where a cost is
shared with home life, only the business share counts (old s. 38(2), now
s. 28(2)); write down how you worked the share out and keep it the same
every year.

| Head (use exactly this name in the expense register) | Typical items | Business share |
|---|---|---|
| Internet and telecom | broadband, mobile plan | 100 % for a line used only for work; a fair share otherwise |
| Electricity | the home-office share, or a separate office meter | by area or a separate meter |
| Office rent or co-working | co-working seat, a rented office | 100 % |
| Software, hosting and subscriptions | IDE, cloud, domains, SaaS, AI tools | 100 % for work tools |
| Computer accessories and repairs | cables, keyboard, mouse, repairs below the capitalisation line | 100 % |
| Repairs and maintenance | office electrical work, servicing office equipment | business share |
| Office supplies and consumables | stationery, printer ink, small items | 100 % |
| Business travel | client visits, conferences | 100 % |
| Conveyance and fuel | local travel, fuel for a vehicle used for work | business share |
| Vehicle insurance | for a vehicle used for work | business share |
| CA, legal and professional fees | the CA's fee, a lawyer reviewing the contract | 100 % |
| Bank and platform charges | bank fees, platform or gateway charges | 100 % |
| Client meals and promotion | entertaining a client, with a note of who and why | 100 % |
| Salaries paid to helpers | an assistant, a bookkeeper | 100 %; paying a relative must be reasonable (old s. 40A(2), now s. 36(2)) |
| Interest on a business loan | a loan taken for the business | 100 % |
| Other | anything else wholly for the work | as applicable |

**Paid in cash above ₹10,000 to one person in a day: not allowed** (old
s. 40A(3), now s. 36(4)). Pay everything by bank or card.

**Assets are depreciated, not expensed** (old s. 32, now s. 33). Anything
that lasts beyond the year goes into a block and is written off at its
rate each year on the reducing balance:

| Block | Rate | Examples |
|---|---|---|
| Computers, including software | 40 % | laptop, desktop, monitor, tablet used for work |
| Plant and machinery | 15 % | AC, inverter and battery, camera, phone |
| Furniture and fittings | 10 % | desk, chair, shelving |

Put to use for **less than 180 days** in the year (for tax year 2026-27,
after 3 October 2026) gets **half the rate** in the first year (s.
33(4)). A common CA practice is to capitalise an item costing more than
about ₹10,000 or with a warranty longer than a year; agree the line with
your CA. If you are GST-registered and claim the input credit, the asset's
cost excludes the GST.

Example: a ₹1,60,000 laptop put to use in August is depreciated ₹64,000
in the first year (40 %), ₹38,400 in the second (40 % of ₹96,000), and so
on. The same laptop bought in November gives ₹32,000 in the first year.

The estimator on the guide page takes these heads and assets line by
line and shows the books profit next to the presumptive one. If you
choose books, `13-keeping-books.md` has the registers and the routine.

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
