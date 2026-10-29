# GST: registering, the LUT, and quarterly returns

## The short version

Your work for a US client is an **export of services**. Exports are
**zero-rated**: once you are registered and have filed a **Letter of
Undertaking (LUT)**, you charge no GST and pay none on your fees. What GST
costs you is **paperwork**, not tax: a compliant invoice for each fee, two
returns a quarter (mostly showing the exports and nil tax), and an LUT
every financial year.

GST law is not affected by the Income-tax Act, 2025; the sections below
are of the CGST and IGST Acts, which carry on as before.

## Do you have to register?

| Your contract fees in the financial year (April to March) | Registration |
|---|---|
| up to **₹20 lakh** (₹10 lakh in Manipur, Mizoram, Nagaland, Tripura) | optional |
| above ₹20 lakh | **mandatory**, within **30 days** of crossing (CGST s. 25(1)) |

- Exports are an inter-state supply (IGST s. 7(5)), which would normally
  force registration whatever the turnover (CGST s. 24(i)); but
  **Notification 10/2017-Integrated Tax** exempts service providers below
  the threshold. That is why the ₹20 lakh line applies to you.
- **Export fees count** towards the ₹20 lakh ("aggregate turnover", CGST
  s. 2(6)). **Salary does not**: count from your first contract invoice.
- In a part year, ₹20 lakh is reached at about ₹1.67 lakh a month over
  twelve months, or proportionately faster over fewer. If you will cross
  it in the first full year, many CAs suggest registering at the start
  rather than mid-year.
- Bank interest and rent from a house are exempt supplies and may count
  in aggregate turnover too. If your fees are near ₹20 lakh, ask your CA.

**Voluntary registration below ₹20 lakh** lets you file an LUT, put a
GSTIN on your invoices, and claim back GST paid on a laptop or co-working
(as a refund, below). It also means two returns every quarter, reverse
charge on foreign software you buy for the work, and late fees if you
miss a filing. If your fees will stay well under ₹20 lakh and you have
little GST on purchases, staying unregistered is simpler and legal.

**Composition scheme**: not available to you; it is barred for anyone
making inter-state supplies (CGST s. 10(2)(c)).

## When is it an export? The five conditions

IGST s. 2(6). All five must hold:

1. You (the supplier) are in India.
2. The client (the recipient) is outside India.
3. The place of supply is outside India. For remote software work the
   default rule applies: the client's location (IGST s. 13(2)).
4. You are paid in **convertible foreign exchange, or in Indian rupees
   where the RBI permits**.
5. You and the client are not branches of one entity.

**Condition 4 and the Deel INR payout.** Deel pays you in rupees from its
correspondent bank's **Rupee Vostro account** (an account a foreign bank
holds in rupees with an Indian bank). Until recently only the "Special
Rupee Vostro Account" route had been clarified (CBIC Circular
202/14/2023-GST), and an ordinary Vostro payout was arguable. **CBIC
Circular 263/09/2026-GST of 26 October 2026** now states that "Rupee
Vostro and SNRR are permissible accounts for receipt of export proceeds"
and that payment into repatriable rupee accounts satisfies s. 2(6)(iv),
relying on the RBI's FEMA 14(R)/2023 receipt rules, which allow export
proceeds from the US in rupees. (Read here from published reproductions;
check the PDF on cbic-gst.gov.in once it is listed there.) The circular
also says meeting condition 4 does not by itself make a supply an export;
the other four still apply, and for a US client they normally do.

**Intermediary**: older articles warn that some services are taxed in
India as "intermediary" services. That place-of-supply rule (IGST s.
13(8)(b)) was deleted by the Finance Act, 2026 from 30 March 2026, and in
any case a contractor writing software for a client supplies his own
service.

**What proves condition 4, per payment**: the invoice; Deel's withdrawal
confirmation; the correspondent bank's **NOC** naming the Rupee Vostro
account and the UTR; your bank's **inward remittance advice (FIRA/BIRC)**
issued against that NOC; and the bank statement line. Keep all five
together (`05-inward-remittance.md`).

## The LUT: file it before the first export invoice

- **Form GST RFD-11** on gst.gov.in: Services → User Services → Furnish
  Letter of Undertaking (LUT). CGST Rule 96A; IGST s. 16(3)(a).
- It is **accepted the moment the ARN is generated** (Circular
  40/14/2018-GST). Download the RFD-11 and the acknowledgement.
- Needs two witnesses (name, address, occupation) and is signed with an
  EVC (OTP).
- **Valid for one financial year.** File the next one in March, or
  before your first invoice in April.
- Without an LUT you must charge 18 % IGST on the export invoice, pay it,
  and claim it back as a refund. Always file the LUT.
- **Late?** File it the day you notice. CBIC circulars allow a delay to
  be condoned where the exports are genuine, but do not rely on it.
- Under the LUT, payment must arrive within **one year** of the invoice
  (Rule 96A(1)(b)), or you pay the IGST with interest. RBI's separate rule
  is stricter (next section); a monthly Deel payout meets both easily.

## RBI's rules for service exporters (new from 1 October 2026)

These are foreign-exchange rules under FEMA, not GST, but they land on
you. **FEMA (Export and Import of Goods and Services) Regulations, 2026**
(FEMA 23(R)/2026-RB, in force 1 October 2026, amended 22 September 2026):

- **Realise the money within 9 months** of the invoice date, or **12
  months** where the export is invoiced or settled in rupees (reg. 5(1)).
- **File an Export Declaration Form (EDF)** with your bank **within 30
  days from the end of the month** in which you raised the invoice (reg.
  3(2)). Services other than software may instead file by the date the
  payment arrives; software exports do not get that option.

How banks will take an EDF for a Deel rupee credit, which their inward
desk never tagged as an export, is still settling. **Ask your bank's
trade-finance desk** in the same e-mail as your first advice request, and
take their answer to your CA.

## The export invoice

If you are registered, each fee needs a tax invoice under **CGST Rule
46**. Deel's own invoice usually lacks your GSTIN, the LUT line and your
own serial number, so the safe default is to **issue your own GST invoice
for each Deel invoice** (same date and amount, citing the Deel invoice
number) and report yours in GSTR-1. Check first whether Deel lets you add
these fields to its invoice. Template: `templates/export-invoice.md`.

It must carry:

- your name, address and **GSTIN**;
- a **serial number unique in the financial year**, up to 16 characters
  (eg `EXP/26-27/001`);
- the date;
- the client's **name, address and country** (in place of a GSTIN);
- a description and **SAC**: **998314** (IT design and development) for
  software development, **998313** (IT consulting and support) for
  advisory work;
- the value (USD, or INR), and IGST: nil;
- the endorsement **"SUPPLY MEANT FOR EXPORT UNDER LETTER OF UNDERTAKING
  WITHOUT PAYMENT OF INTEGRATED TAX"**;
- your LUT's ARN and date (not required by the rule, but refund officers
  look for it);
- your signature, or none if it is an electronic invoice.

Issue it within 30 days of the service (Rule 47). E-invoicing (IRN) does
not apply below ₹5 crore of turnover.

**Invoice currency and the rupee value** in your return: a USD invoice is
normal. For GSTR-1 you report the rupee value; the common practice is the
reference rate on the invoice date, or the rupee amount actually
credited. Agree one with your CA, use the same figure for income tax, and
keep it every year.

## Returns: quarterly, under QRMP

With turnover under ₹5 crore you can choose the **Quarterly Return
Monthly Payment (QRMP)** scheme. Choose it at registration, or by the
last day of the first month of a quarter for that quarter.

| Return | QRMP (quarterly) | Monthly |
|---|---|---|
| **GSTR-1** (your sales; exports in **Table 6A**, type "without payment") | by the **13th** of the month after the quarter | by the 11th of the next month |
| **GSTR-3B** (summary and payment; exports in **Table 3.1(b)**) | by the **22nd or 24th** of the month after the quarter, by state | by the 20th |
| **PMT-06** (monthly payment) | by the 25th of months 1 and 2, **only if** you owe something (eg reverse charge) | not used |

**22nd** for Chhattisgarh, Madhya Pradesh, Gujarat, Maharashtra,
Karnataka, Goa, Kerala, Tamil Nadu, Telangana, Andhra Pradesh, Daman and
Diu, Dadra and Nagar Haveli, Puducherry, Andaman and Nicobar, Lakshadweep.
**24th** for all other states and union territories, including Delhi,
Haryana, Punjab, Uttar Pradesh, Rajasthan, West Bengal.

Quarter dates for a QRMP filer:

| Quarter | GSTR-1 | GSTR-3B |
|---|---|---|
| April to June | 13 July | 22 / 24 July |
| July to September | 13 October | 22 / 24 October |
| October to December | 13 January | 22 / 24 January |
| January to March | 13 April | 22 / 24 April |

Things that changed recently and catch people:

- **File GSTR-1 first, and get it right.** Since the July 2025 period the
  sales figures in GSTR-3B come from GSTR-1 and cannot be edited there;
  corrections go through **GSTR-1A** before filing 3B.
- **No return can be filed more than three years after its due date.**
- **GSTR-9 (annual return) is not required** up to ₹2 crore turnover
  (Notification 15/2025-CT).
- A quarter with exports is **not a nil return**, so SMS filing is out;
  file on the portal.
- **Late fee**: ₹50 a day (₹20 for a nil return), capped at ₹2,000 per
  return at your turnover (₹500 for nil). It appears in the next 3B and
  cannot be edited away.

### Portal habits that save trouble

- **Never type an inner portal URL** (a `return.gst.gov.in/...` address):
  it ends the session with "Access Denied". Log in and click through the
  menus from the dashboard.
- Open **Services → Returns → Returns Dashboard**, pick the financial
  year, quarter and month, and the tiles for GSTR-1 and 3B appear.
- In 3B, check each pre-filled tile before saving: **3.1(b)** comes from
  GSTR-1; **Table 4** may show GST that a supplier charged on your GSTIN
  (eg a laptop); **5.1** may hold a late fee.
- "Proceed to File" stays grey until the "additional cash required"
  column (scroll the payment table right) is zero.
- Pay any challan by **net banking**: a card payment lands on the card
  with the gateway's margin added and never matches the challan.
- Download and keep, every quarter: the filed GSTR-1 and GSTR-3B PDFs,
  any challan receipt. Every year: the RFD-11 and its acknowledgement.

## Reverse charge on software you buy from abroad

Once registered, a foreign service you buy (GitHub, JetBrains, AWS, a
Google Workspace or AI-tool subscription billed from outside India) is an
**import of services**, and **you** pay 18 % IGST on it under reverse
charge (IGST s. 5(3), Notification 10/2017-IT(Rate)). Report it in 3B
Table 3.1(d) and take the same amount as input credit in Table 4A(2).
For an exporter with no output tax, that credit just sits in your ledger,
so reverse charge is real cash out, recoverable only through a refund
(below).

Two ways to reduce it: buy from a vendor that bills you from its Indian
entity with GST on your GSTIN (an ordinary purchase), and keep personal
subscriptions on a separate account from business ones. Whether a fee
Deel deducts from you falls under reverse charge depends on which Deel
entity bills it; for a plain INR bank withdrawal there is usually no
separate fee, only an exchange margin. Ask your CA.

## Input credit and refunds

GST you pay on business purchases (laptop, monitor, co-working, CA fees,
reverse-charge tax) is **input tax credit** if the invoice carries your
GSTIN and shows in your GSTR-2B. With exports under an LUT you have no tax
to set it against, but you can claim it back as a **refund of unutilised
credit** (CGST s. 54(3), Rule 89, form **RFD-01**, with invoice-wise
details and the remittance advices). Most small exporters claim once a
year, if at all; below a few thousand rupees it is not worth the
scrutiny. The claim must be made within two years.

## Stopping

If you return to employment or drop below the threshold, cancel with
**REG-16**, file every pending return first, and file the final return
**GSTR-10** within three months of the cancellation order.

## For your CA

- Register now, or wait for ₹20 lakh?
- Does the NOC's account description fall within Circular 263/09/2026?
  Any step needed for rupee credits received before 26 October 2026?
- Is a Deel invoice plus your own GST invoice the right pairing?
- Which rupee value goes into GSTR-1?
- How will your bank take the EDF?
- Is a return with only zero-rated exports charged the nil late-fee rate?
