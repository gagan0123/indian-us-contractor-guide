# Inward remittance: proving the money came from abroad

## Why this paper matters

Two things rest on proof that each payment came from outside India:

- **GST**: the export is zero-rated only if you were paid in foreign
  exchange or in rupees the RBI permits (`03-gst.md`, condition 4). An LUT
  also requires payment within a year, and a GST refund claim asks for a
  remittance certificate per invoice.
- **FEMA**: from 1 October 2026 a service exporter must realise each
  invoice within 9 or 12 months and file an EDF with the bank.

Income tax does not need these papers to tax you, but your CA will use
them to tie invoices to bank credits.

## The names you will meet

| Term | What it is |
|---|---|
| **FIRC** | Foreign Inward Remittance Certificate. The old name; many people still use it for any of these |
| **FIRA** | Foreign Inward Remittance Advice. What banks mostly issue now, often electronically (e-FIRA) for SWIFT credits |
| **BIRC** | Bank (Inward) Remittance Certificate; for a platform payout, the advice your bank issues against the correspondent's NOC |
| **NOC for issuance of BIRC** | Issued by the **correspondent bank** that paid you on Deel's behalf. It says the correspondent has not and will not issue a certificate, and that the money came from a non-resident Rupee Vostro account. Your bank needs it before it will issue its advice |
| **Purpose code** | RBI code for why the money was sent. P0802 (software consulting and implementation) is typical for contract development; P0807 is off-site software export under SOFTEX. A wrong code (a family-maintenance or goods code) is a problem to fix early |
| **UTR** | The RTGS/NEFT reference of the credit, on your statement and the NOC |
| **Rupee Vostro account** | A rupee account a foreign bank holds with an Indian bank; Deel's payouts in INR come from one |
| **EDF** | Export Declaration Form, filed with your bank under FEMA from 1 October 2026 |
| **e-BRC** | DGFT's electronic realisation certificate, needed for export incentives under the Foreign Trade Policy. Not needed by a contractor who claims none |

## Why your bank does not issue it by itself

A SWIFT wire from abroad reaches your bank's inward desk as a foreign
message, and the bank issues an advice automatically. A Deel INR payout
reaches your account as a **domestic RTGS** from an Indian correspondent
bank. Your bank's inward desk never sees a foreign message, so it issues
nothing unless asked, and it asks for the correspondent's NOC first.

## The steps, each month

1. **When you add the bank withdrawal method on Deel, ask for the NOC.**
   Deel says it cannot provide one otherwise. Do it once, at setup.
2. **Withdraw**; the credit lands next working day. Note the UTR.
3. **Three or four days later**, download the **withdrawal confirmation**
   and the **NOC** from the transaction on Deel.
4. **E-mail your bank's inward remittance / trade-finance desk**, not the
   branch, with the NOC attached and the details as the NOC prints them:
   `templates/bank-advice-request.md`. Reply on the same thread each
   month.
5. **Receive the advice** (by e-mail and often by courier). It may print
   no USD amount and no exchange rate for a rupee credit; that is normal.
   Deel's help centre notes that once the bank has the documents it
   generates an **Inward Remittance (IRM) number** in RBI's Export Data
   Processing and Monitoring System (EDPMS). Ask the desk for the IRM
   number: it is what your EDF and the export record are matched
   against.
6. **File the set** in that month's folder (`checklists/monthly.md`).
7. **EDF**: within 30 days of the end of the invoice month, as your bank
   asks (`03-gst.md`). Raise it in the first e-mail so you learn the
   bank's process before the deadline matters.

People report the first request taking one to two weeks, mostly when it
went to the branch or lacked the NOC. Once the desk knows you, a day is
common.

## If the bank will not issue it

Some banks hold the credit itself first: Deel's help centre says
IndusInd may ask for the contract and invoices before crediting, adding up
to ten business days. Answer promptly, and describe the payment as
software consultancy, never salary.

Some banks resist issuing an advice for a rupee credit even with an NOC.
Ask for the refusal in writing, keep the NOC, the withdrawal confirmation
and the statement line, and take them to your CA. Courts have accepted
other evidence of realisation (a CA certificate with bank statements,
for instance) for GST refunds, but the advice is the clean path. If the
bank stays unhelpful, a bank with an active trade-finance desk is worth
switching to for the work account.
