# Export invoice template (GST-registered, under LUT)

Fill once with your fixed details, then copy per invoice. Produce a PDF
from it (any word processor, or a spreadsheet). Every field below is
needed under CGST Rule 46 unless marked optional.

---

**TAX INVOICE**

**SUPPLY MEANT FOR EXPORT UNDER LETTER OF UNDERTAKING WITHOUT PAYMENT OF INTEGRATED TAX**

| | |
|---|---|
| Invoice no. | `EXP/26-27/001` (unique in the financial year, up to 16 characters) |
| Invoice date | `DD-MM-YYYY` |
| Service period | `01-MM-YYYY to DD-MM-YYYY` |
| LUT ARN and date | `AD<...>` dated `DD-MM-YYYY` (financial year `2026-27`) |
| Platform reference (optional) | Deel invoice `<number>` |

**Supplier**
`<Your full name>`
`<Address of principal place of business>`
GSTIN: `<15 characters>`  ·  PAN: `<PAN>`
State: `<State>` (code `<nn>`)

**Recipient (outside India)**
`<Client legal name>`
`<Client address>`
Country: **United States of America**
Place of supply: **Outside India** (IGST Act s. 13(2))

| # | Description | SAC | Qty | Rate | Amount |
|---|---|---|---|---|---|
| 1 | Software development services for `<project>` for `<period>` | 998314 | 1 | USD `<x>` | USD `<x>` |

| | |
|---|---|
| Taxable value | USD `<x>` (INR `<y>` at `<rate>` on `<date>`, `<source of rate>`) |
| IGST | Nil (0 %, zero-rated export under LUT) |
| **Total** | **USD `<x>`** |

Amount in words: `<US dollars ... only>`

Payment received through `<platform>` to `<bank>`, A/c `<last 4 digits>`.

`<Signature, or: "This is a computer-generated invoice.">`

---

## Notes

- Use **998313** instead of 998314 for consulting or support without
  development.
- If the contract is in INR, show INR throughout and drop the rate line.
- The INR figure must match what you report in GSTR-1 and, by the
  method you chose, in your income-tax computation.
- Without an LUT the endorsement becomes "... ON PAYMENT OF INTEGRATED
  TAX" and you charge 18 % IGST. File the LUT instead.
