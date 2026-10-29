# Deel: setting up and the monthly routine

This chapter covers the Deel **Contractor** model: you sign a contract with
the client on Deel, invoices are raised on Deel, the client pays Deel, and
you withdraw to your own bank. Deel is a payment and paperwork platform
here, not your employer. If your offer says Deel **EOR** (Employer of
Record), Deel's Indian entity employs you, you get a salary with TDS and a
Form 16, and most of this guide does not apply. Check which one it is
before you sign.

Deel's help centre changes often and menu names move. Where this chapter
names a screen, treat it as a pointer and confirm it in the app. Anything
marked **(check)** was not confirmed from a Deel page when this was
written.

## Before the first invoice

| # | Step | Why it matters |
|---|---|---|
| 1 | Accept the client's invite and create the account in your **legal name exactly as on your PAN and bank account** | A withdrawal to an account that is not in your own name is rejected. A business (current) account in a trade name needs extra "For Further Credit" papers |
| 2 | Complete identity verification (a selfie and an ID document; a passport is accepted, other IDs **(check)**) | Payouts are blocked until it clears |
| 3 | Review the contract before signing: scope, IP assignment, termination notice, payment cycle, **contract currency**, who bears Deel or bank fees, governing law | See `09-contract-and-invoicing.md` for the clauses to read closely |
| 4 | Fill the **W-8BEN** (the US tax form for a non-US individual). Put your **PAN in the foreign TIN field** and India as country of residence. Save the signed PDF | It tells the client no US tax should be withheld. Services performed entirely in India are generally not US-source income, so no US withholding arises; whether to fill the treaty claim in Part II (and cite Article 15 or Article 7 of the India-US treaty) is a point to settle with your CA. A W-8BEN stays valid to the end of the third calendar year after you sign it, unless your circumstances change |
| 5 | Add the **bank transfer withdrawal method** to your INR savings or current account, and **tell Deel you need the NOC for FIRC at that moment** | Deel says it cannot provide the NOC if you did not ask for it when adding the method. Without the NOC your bank will not issue the inward remittance advice, which is your export evidence (see `05-inward-remittance.md`) |
| 6 | Ask Deel support which **purpose code** it sends the money under, and ask your bank which code it expects for your work | A wrong code (for example one meant for goods, or for a family transfer) stalls the advice and needs a corrected NOC. Software consulting is usually P0802; P0807 is off-site software export under SOFTEX. Pick with your bank and CA |
| 7 | Ask your bank, before the first credit, **which desk issues inward remittance advice** (usually trade finance or forex operations, not the branch) and its e-mail address | The single biggest delay people report is writing to the branch |
| 8 | Settle the GST position with your CA (`03-gst.md`): register or not, file the LUT **before** the first export invoice, and whether Deel's invoice can carry your GSTIN and the LUT line **(check in the app or with Deel support)** | If it cannot, you issue your own GST invoice for each Deel invoice; see the template in `templates/` |
| 9 | Decide manual or automatic withdrawal | Monthly manual withdrawal keeps one credit per invoice, which makes the paper trail simple |

## Contract types

Deel offers three contractor payment shapes: **fixed rate** (a set amount
per cycle; the invoice is generated for you), **pay as you go** (you
submit hours or work each cycle) and **milestone** (paid when a milestone
is approved) **(check the current names)**. The client sets an approval
policy: under some settings a fixed-rate invoice flows without the
client's approval and only extras (bonus, overtime) wait.

## Withdrawal methods and what they mean for tax

| Method | Deel fee (as reported, may change) | What you need to know |
|---|---|---|
| Local bank transfer in INR | No Deel fee reported; the exchange rate carries a margin, and a provider fee may apply | Arrives by RTGS/NEFT from Deel's Indian correspondent bank, which debits a rupee Vostro account. **The default for most Indian contractors**, and the only one that leaves nothing held abroad |
| SWIFT transfer | about USD 5 to 25, plus intermediary bank charges | The bank sees a foreign wire and usually issues the advice itself |
| Deel Balance left un-withdrawn, Deel Card, Deel USD account | no Deel fee on the card | Money held outside India. **Report it in Schedule FA** of your ITR (`06-foreign-assets.md`), and ITR-4 cannot carry Schedule FA |
| Wise, Payoneer, Revolut, crypto | provider fees; Payoneer about 1 % | Same Schedule FA point; and a wallet balance converted later through a provider can change who the remitter is on your bank's advice |

The pop-up before you confirm a withdrawal shows the fee and the rate.
Note it: the difference between that rate and the day's reference rate is
the real cost of the method.

A failed withdrawal returns to your Deel balance in three to five
business days. If money does not arrive, the **Trace ID** on the
transaction's confirmation is what Deel support needs.

## The monthly routine

1. **Invoice.** Deel generates the invoice (fixed rate) or you submit it.
   The client approves; the cycle pays into your Deel balance.
2. **Withdraw** to your bank. Deel mails that the money is on the way;
   the credit lands as an RTGS line, usually next working day. Your bank
   may send no special alert for it.
3. **Download, three to four days later**, from Transactions → the
   withdrawal (**check** the menu): the **Withdrawal Confirmation** and the
   **NOC** (since late 2023 often titled "NOC for issuance of BIRC"). Deel
   mails when the NOC is ready.
4. **Request the bank's advice**: one e-mail to the inward remittance or
   trade-finance desk, with the NOC attached and the details as the NOC
   prints them. Template: `templates/bank-advice-request.md`.
5. **File the set together** in that month's folder: the Deel invoice,
   your own GST invoice if you issue one, the withdrawal confirmation, the
   NOC, the bank's advice, and the bank statement line. One credit, one
   folder, five documents. `checklists/monthly.md` has the list.
6. **GST**: the invoice goes into that quarter's GSTR-1 as an export
   under LUT (`03-gst.md`).

## Once a year, download for your CA

- Every invoice of the financial year (April to March).
- Every withdrawal confirmation and NOC.
- Deel's transaction history or earnings report for April to March
  (**check** the report's name).
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
