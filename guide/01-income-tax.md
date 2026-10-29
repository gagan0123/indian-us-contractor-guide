# Income tax as a contractor: tax on profit, not on salary

## The one idea that changes

As an employee you were taxed on your **salary**, your employer deducted
the tax every month (TDS), and a Form 16 told you what had been paid. As a
contractor you are taxed on the **profit of your profession**: what you
billed, less what it cost you to earn it. Nobody deducts tax for you. A US
client or Deel has no duty to deduct Indian TDS, so no tax shows against
the fee in your Form 26AS / Form 168, and you pay it yourself as **advance
tax** during the year.

There are two ways to work out that profit:

- **Presumptive (old s. 44ADA, now s. 58 of the Income-tax Act, 2025)**:
  the law deems 50 % of your receipts to be profit. No expense accounting,
  no audit, a simpler return. Most software contractors under ₹75 lakh use
  this.
- **Actual books**: you keep accounts, profit is receipts minus real
  expenses (laptop depreciation, internet, co-working, software, CA fees),
  and above ₹50 lakh of receipts you need a tax audit.

`02-presumptive-or-books.md` helps you choose. This chapter covers what is
common to both.

## Which law: the 2025 Act

**Tax year 2026-27 (1 April 2026 to 31 March 2027) is the first year under
the Income-tax Act, 2025** and the Income-tax Rules, 2026. The rules
mostly carried over, but every section is renumbered, "previous year" and
"assessment year" became one "tax year", and many forms were renamed
(Form 16 is now **Form 130**; Form 26AS is now **Form 168**; the regime
option Form 10-IEA is now **Form 44**). Articles, CAs and the portal will
use both numberings for a while, so this guide gives both: "old s. 44ADA,
now s. 58". The **Finance Act, 2026** amended the new Act before its first
year began; the changes that matter to you are flagged below.

## How your first year adds up

In the year you switch, one return carries both:

```
Salary (April to your last day)            from Form 130 (old Form 16)
  less standard deduction                  ₹75,000 new regime / ₹50,000 old
+ Profit of profession                     50 % of receipts (presumptive)
                                           or receipts - expenses (books)
+ Interest, dividends, capital gains, rent  as before
= Total income  →  tax at slab rates  →  less rebate  →  + 4 % cess
  less salary TDS your employer deducted
  less advance tax you paid
= tax due with the return (or refund)
```

The standard deduction applies in full to the salary months; it is not
pro-rated.

## Rates for tax year 2026-27

**New regime** (the default; old s. 115BAC, now s. 202(1)):

| Total income | Rate |
|---|---|
| up to ₹4 lakh | nil |
| ₹4 to 8 lakh | 5 % |
| ₹8 to 12 lakh | 10 % |
| ₹12 to 16 lakh | 15 % |
| ₹16 to 20 lakh | 20 % |
| ₹20 to 24 lakh | 25 % |
| above ₹24 lakh | 30 % |

**Rebate** (old s. 87A, now s. 156): under the new regime, if total income
is ₹12 lakh or less, tax up to ₹60,000 is rebated, so the tax is nil, with
marginal relief just above ₹12 lakh. It applies to professional income
too: presumptive receipts of ₹24 lakh give ₹12 lakh of income and nil tax.
It does not cover special-rate capital gains.

**Old regime** (below 60): up to ₹2.5 lakh nil, ₹2.5 to 5 lakh 5 %, ₹5 to
10 lakh 20 %, above ₹10 lakh 30 %; rebate up to ₹12,500 if income is ₹5
lakh or less.

**Surcharge** above ₹50 lakh of income (10 %, then 15 % above ₹1 crore,
25 % above ₹2 crore), and **4 % health and education cess** on tax plus
surcharge, in both regimes.

## Old or new regime: the rule is different for you now

A salaried person with no business income picks a regime **each year in
the return**. Once you have professional income, that freedom narrows
(old s. 115BAC(6), now **s. 202(4)(a)**):

- The new regime is the default.
- To use the old regime you file **Form 44** (old 10-IEA) **on or before
  the return due date**. The choice then carries forward.
- You can come back to the new regime later, but **only once**: after
  that you can never opt out again while you have professional income.

Your own EPF contribution from the salary months counts in 80C under the
old regime (inside the same ₹1.5 lakh). Your employer's EPF contribution
is not taxed unless employer EPF and NPS contributions together exceed
₹7.5 lakh in the year; the employer's NPS contribution is deductible in
both regimes (old s. 80CCD(2), now s. 124(1)-(2)).

So treat the regime as a multi-year decision. Under the presumptive
scheme your profit is already halved; the old regime's deductions (80C
₹1.5 lakh, now s. 123; 80D health insurance ₹25,000 for your family and
₹25,000 more for parents, ₹50,000 each if senior, now s. 126; NPS
₹50,000 extra under 80CCD(1B), now s. 124(3); home-loan interest) rarely
beat the new regime's lower slabs and ₹12 lakh rebate. Run both in the
calculator on the guide page, and decide with your CA. Whatever you told
your employer for TDS does not bind the return.

## Advance tax: you are your own payroll department

You must pay advance tax if the tax for the year, after TDS, is **₹10,000
or more** (old s. 208, now s. 404).

| Due by | Books route: cumulative share of the year's tax | Presumptive route |
|---|---|---|
| 15 June | 15 % | nothing required |
| 15 September | 45 % | nothing required |
| 15 December | 75 % | nothing required |
| 15 March | 100 % | **100 %**, in one go |

(old s. 211, now s. 408; presumptive single instalment old s. 211(1)(b),
now s. 408(2). Anything paid by 31 March counts as advance tax.)

**Interest if you fall short** (old ss. 234B and 234C, now ss. 424 and
425):

- **Late instalment**: 3 % of the shortfall at each of 15 June, 15
  September and 15 December, and 1 % at 15 March. A presumptive filer
  pays only the 1 % on any shortfall at 15 March.
- **Less than 90 % paid by 31 March**: 1 % a month on the shortfall from 1
  April until you pay.
- **First-year relief** (s. 425(4), old 234C proviso): no instalment
  interest on a shortfall caused by professional income "arising for the
  first time", if you pay that tax in the remaining instalments. Whether
  "first time" covers someone who never had business income before
  (likely you) is a point to confirm with your CA.

**Pay even on the presumptive scheme as you go.** The law lets you wait
until 15 March, but paying a share each quarter keeps the money from
being spent. Pay on the e-filing portal: e-Pay Tax → Income tax → advance
tax, for the tax year 2026-27. Save every challan.

**Mid-year estimate, in four steps:** at each date, (1) project the full
year: actual salary plus expected receipts (× 50 % if presumptive, minus
expected expenses if on books) plus other income; (2) compute the tax with
cess; (3) subtract salary TDS your employer has deducted or will deduct;
(4) pay that date's cumulative share, less what you have already paid.

### A worked example (illustrative numbers)

New regime. Salary April to July 2026: ₹8,00,000, less ₹75,000 standard
deduction = ₹7,25,000. Deel receipts August 2026 to March 2027: ₹40,00,000,
presumptive profit ₹20,00,000. Total income ₹27,25,000.

Tax: ₹20,000 + 40,000 + 60,000 + 80,000 + 1,00,000 + 30 % of ₹3,25,000
(₹97,500) = ₹3,97,500; cess ₹15,900; **₹4,13,400**. The employer saw only
₹7,25,000 of salary (rebated), so it deducted no TDS, and the whole
₹4,13,400 is advance tax, due by 15 March 2027. That is about **10 % of
the receipts**; paying ₹50,000 a month from the first credit covers it.

## The return

- **Form**: **ITR-4** (Sugam) if you are on the presumptive scheme, total
  income is ₹50 lakh or less, and you hold **no asset outside India**.
  Otherwise **ITR-3**, which also carries presumptive income. A Deel
  balance, a Deel Card, a Wise or Payoneer balance, or US shares or RSUs
  from a previous employer all make it ITR-3 (`06-foreign-assets.md`).
  The forms for tax year 2026-27 are notified in spring 2027; check then.
- **Due date**: the Finance Act, 2026 moved it to **31 August** for
  anyone with business or professional income whose accounts are not
  audited (s. 263(1)(c)). So **31 August 2027** for tax year 2026-27 on the
  presumptive scheme or unaudited books, and **31 October 2027** if you are
  audited (audit report by 30 September). Salary-only filers stay on 31
  July. **Form 44, if you want the old regime, goes in by the same date.**
- **Late**: a belated return is allowed until 31 December 2027, with a
  late fee of ₹5,000 (₹1,000 if income is ₹5 lakh or less; old s. 234F,
  now s. 428(a)) and 1 % a month interest on unpaid tax (old 234A, now s.
  423). A revised return can now be filed up to 12 months after the tax
  year ends (31 March 2028), with a fee of ₹1,000 or ₹5,000 if filed after
  the ninth month (now s. 263(5) and s. 428(b)).
- **Forgot something?** An **updated return** (ITR-U; old s. 139(8A), now
  s. 263(6)) can add income up to 48 months after the end of the year
  following the tax year, at an extra 25 %, 50 %, 60 % or 70 % of the tax
  and interest depending on how late. It cannot reduce tax or raise a
  refund.

## Before you file, reconcile

Download the **AIS** (Annual Information Statement) and **Form 168**
(formerly 26AS) from the e-filing portal and check them against Form 130
from your employer, your bank interest, and your Deel credits. The Deel
fee will usually not appear in either; that is expected. If it does
(for example, TDS by an Indian entity), make sure the receipts you report
are at least what is shown. Give feedback on the AIS portal for any wrong
entry.

## US tax

None, in the normal case. Under the India-US tax treaty (Article 15) and
US source rules, fees for work you do while physically in India are
taxable only in India. The W-8BEN you give Deel records that you are not
a US person. If you work from the US for 90 days or more in a year, or
have a fixed base there, take advice before you go.

## For your CA

- Is your work a "profession" eligible for s. 58 (information technology
  is now named in s. 62(4)), or a business?
- Does the s. 425(4) first-year relief apply to you?
- Which rate converts USD invoices to rupees, and is income booked on
  invoice date or credit date?
- Can Form 44 be filed with a belated return? (Assume not.)
