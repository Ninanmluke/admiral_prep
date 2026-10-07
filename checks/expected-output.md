# Expected output for AE-3

The current severe-only requirement produces two records:

| USUBJID | AETERM | AESEV |
|---|---|---|
| 003 | Neutropenia | SEVERE |
| 006 | Sepsis | SEVERE |

Expected record count: **2**

If the requirement changes, this file must be updated and reviewed with the implementation and automated tests.
