# ERPNext EXIM & Customs Landed Cost Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Customs Act 1962](https://img.shields.io/badge/Customs-CBIC%20Compliant-orange.svg)](https://cbic.gov.in)

Enterprise export-import (EXIM) clearing and customs landed valuation engine modeled after high-volume trading enterprises.

## Features
- **CBIC Customs Duty Formula:** Basic Customs Duty (BCD), Social Welfare Surcharge (SWS), and Integrated GST (IGST) compounded landed assessment.
- **Export Incentives:** Duty Drawback (DBK) and Remission of Duties and Taxes on Exported Products (RoDTEP) claim settlement.
- **Letter of Credit (LC) Workflow:** Sight/Usance bank guarantees and container Bill of Lading (BL) reconciliation.

## Installation & Tests
```bash
python3 -m unittest discover tests
```
