# Deel: setting up and the monthly routine

This chapter covers the Deel **Contractor** model: you sign a contract with
the client on Deel, invoices are raised on Deel, the client pays Deel, and
you withdraw to your own bank. Deel is a payment and paperwork platform
here, not your employer. If your offer says Deel **EOR** (Employer of
Record), Deel's Indian entity employs you, you get a salary with TDS and a
Form 16, and most of this guide does not apply. Check which one it is
before you sign.

Menu paths and fees below were read from Deel's help centre on 29
October 2026 (articles listed in `sources.md`). Deel moves screens often;
if a path has changed, search the help centre for the article title.

## Before the first invoice

| # | Step | Why it matters |
|---|---|---|
| 1 | Accept the client's invite and create the account in your **legal name exactly as on your PAN and bank account** | A withdrawal to an account that is not in your own name is rejected. A business (current) account in a trade name needs extra "For Further Credit" papers |
| 2 | Complete identity verification: Profile settings → Verification → Verify. Deel's partner Veriff asks for a selfie and a photo of a government-issued photo ID; if Veriff fails you can request manual review (about one business day) | You cannot withdraw until it clears, and some clients require it before you can even sign the contract |
| 3 | Review the contract before signing: scope, IP assignment, termination notice, payment cycle, **contract currency**, who bears Deel or bank fees, governing law | See `09-contract-and-invoicing.md` for the clauses to read closely |
| 4 | Fill the **W-8BEN** (the US tax form for a non-US individual; Deel names "a sole proprietor in India" as a W-8BEN filer): Finance → Tax Documents → Create US tax forms. Put your **PAN in the foreign TIN field** and India as country of residence. Download the PDF from the same tab | It tells the client no US tax should be withheld. Services performed entirely in India are generally not US-source income, so no US withholding arises; whether to fill the treaty claim in Part II (and cite Article 15 or Article 7 of the India-US treaty) is a point to settle with your CA. A W-8BEN stays valid to the end of the third calendar year after you sign it, unless your circumstances change |
| 5 | Add the **bank transfer withdrawal method** to your INR savings or current account, and **tell Deel you need the NOC for FIRC at that moment** | Deel says it cannot provide the NOC if you did not ask for it when adding the method. Without the NOC your bank will not issue the inward remittance advice, which is your export evidence (see `05-inward-remittance.md`) |
| 6 | Know the **purpose** your payout carries. Deel's help centre says INR payouts are sent as "Software consultancy/implementation (other than those covered in SOFTEX form)", which is purpose code **P0802**. If your bank calls to ask what the credit is, say exactly that, **never "salary"** | A salary description contradicts the export and stalls the advice. Some banks (Deel names IndusInd) hold the credit and ask for the contract and invoices first, adding up to ten business days: keep both ready |
| 7 | Ask your bank, before the first credit, **which desk issues inward remittance advice** (usually trade finance or forex operations, not the branch) and its e-mail address | The single biggest delay people report is writing to the branch |
| 8 | Settle the GST position with your CA (`03-gst.md`): register or not, and file the LUT **before** the first export invoice | Deel's standard invoice has no field for your GSTIN or the LUT line, and only the client can add tax lines. But you can **upload your own invoice, which replaces Deel's**: Finance → Invoices → the invoice's options menu → Replace with custom invoice. Upload your GST invoice (`templates/export-invoice.md`) there each cycle, and Deel's record and your tax invoice are one document |
| 9 | Decide manual or automatic withdrawal: Account settings → Withdrawal Methods, where you set the preferred method and can auto-withdraw all or part of each payment | Automatic withdrawal of 100 % to the bank keeps one credit per invoice and nothing left abroad |

## Contract types

Deel has three independent-contractor contracts: **Fixed Rate** (a set
amount each pay cycle; the invoice is generated automatically), **Pay As
You Go** (paid on the days, hours or tasks you submit) and **Milestone**
(paid when a milestone is approved; no regular invoice cycle). The
client sets an approval policy; under some settings a fixed-rate invoice
flows without approval and only extras (bonus, overtime) wait. Funds
reach your Deel balance on the contract's due date if the client has
paid; the contract's details page shows the invoice cycle, and Finance →
Transactions shows incoming payments with a payment tracker. Both sides
must sign before a contract is active.

## Withdrawal methods and what they mean for tax

| Method | Deel fee (help centre, updated 16 October 2026) | What you need to know |
|---|---|---|
| Local bank transfer in INR | **$0** (minimum $10); a provider fee may apply in some currencies, and the exchange rate carries a margin | Arrives by RTGS/NEFT from Deel's Indian correspondent bank, which debits a rupee Vostro account. **The default for most Indian contractors**, the only method Deel issues the NOC for, and the only one that leaves nothing held abroad |
| SWIFT transfer | $5, capped at $10 (minimum $100), plus intermediary bank deductions | The bank sees a foreign wire; but Deel's NOC is not available for it |
| Deel balance left un-withdrawn, Deel Card | Deel Card $0 | Money held outside India. **Report it in Schedule FA** of your ITR (`06-foreign-assets.md`), and ITR-4 cannot carry Schedule FA |
| Wise, Revolut ($0), Payoneer (1 %, minimum $12), PayPal (2.5 %), crypto | as shown | Same Schedule FA point; no Deel NOC; and the remitter on your bank's advice becomes the provider |

The pop-up before you confirm a withdrawal shows the fee and the rate.
Note it: the difference between that rate and the day's reference rate is
the real cost of the method.

Deel adds a $5 fee to any same-currency cross-border withdrawal. A
failed withdrawal returns to your Deel balance in three to five business
days. If money does not arrive by the estimated date, report it from the
transaction tracker; the **Trace ID** on the withdrawal's confirmation
statement (Finance → Transactions → the withdrawal) is what your bank and
Deel support need.

## The monthly routine

1. **Invoice.** Deel generates the invoice (fixed rate) or you submit it.
   The client approves; the cycle pays into your Deel balance.
2. **Withdraw** to your bank. Deel mails that the money is on the way;
   the credit lands as an RTGS line, usually next working day. Your bank
   may send no special alert for it.
3. **Download, a few business days later**, from Finance → Transactions
   → the withdrawal → Withdrawal Details: the **withdrawal confirmation**
   statement and the **NOC** (since late 2023 often titled "NOC for
   issuance of BIRC"). Deel mails when the NOC is ready.
4. **Request the bank's advice**: one e-mail to the inward remittance or
   trade-finance desk, with the NOC attached and the details as the NOC
   prints them. Template: `templates/bank-advice-request.md`.
5. **File the set together** in that month's folder: the invoice (your
   GST invoice, uploaded to Deel in place of its own), the withdrawal confirmation, the
   NOC, the bank's advice, and the bank statement line. One credit, one
   folder, five documents. `checklists/monthly.md` has the list.
6. **GST**: the invoice goes into that quarter's GSTR-1 as an export
   under LUT (`03-gst.md`).

## Once a year, download for your CA

- Every invoice of the financial year (April to March).
- Every withdrawal confirmation and NOC.
- Deel's transaction list for April to March (Finance → Transactions).
  Invoices are under Finance → Invoices.
- Your Deel balance at **31 December** and at **31 March**, and the
  highest balance during the calendar year, if you ever held money there
  (Schedule FA works on the calendar year).
- The signed contract, any amendments, and the W-8BEN.

Deel issues no Form 1099 to a non-US contractor who filed a W-8BEN. You
do not need one: your Indian return is built from your invoices and bank
credits.

## Things people get wrong

1. Not asking for the NOC when adding the bank method.
2. Writing to the branch instead of the trade-finance desk, or sending
   the request without the NOC attached.
3. A wrong purpose code on the remittance.
4. A bank account whose name does not match the Deel profile.
5. Leaving money in the Deel balance or on the Deel card across 31
   December and forgetting Schedule FA.
6. Not deciding how a USD invoice becomes a rupee figure. Two readings
   are common: the INR your bank actually credited (simple, and it
   matches what GSTR-1 shows if you report the credited value), or the
   invoice converted at a reference rate, with the platform's fee and
   exchange margin booked as a cost. Agree one with your CA in the first
   year, write it down in your year folder, and keep it every year after.
