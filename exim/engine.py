"""Export-Import (EXIM) Customs, Letter of Credit & Landed Duty Calculation Engine."""

from datetime import datetime, date
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class LetterOfCredit:
    lc_number: str
    issuing_bank: str
    beneficiary_name: str
    lc_amount_foreign_currency: float
    currency: str
    issue_date: str
    expiry_date: str
    is_active: bool = True


@dataclass
class CustomsLandedCostAssessment:
    assessable_value_inr: float
    basic_customs_duty_bcd: float
    social_welfare_surcharge_sws: float
    integrated_gst_igst: float
    total_customs_duty_payable: float
    total_landed_cost_inr: float


@dataclass
class DutyDrawbackClaim:
    shipping_bill_number: str
    fob_value_inr: float
    drawback_rate_pct: float
    eligible_drawback_inr: float
    rodtep_rate_pct: float
    eligible_rodtep_inr: float
    total_export_incentive_inr: float


class EximCustomsEngine:
    """Manages Cross-border EXIM compliance, customs duties, and export incentives."""

    def assess_import_customs(
        self,
        cif_value_foreign: float,
        exchange_rate_cbic: float,
        bcd_rate_pct: float = 7.5,
        sws_rate_pct: float = 10.0,  # 10% of BCD
        igst_rate_pct: float = 18.0
    ) -> CustomsLandedCostAssessment:
        assessable_inr = round(cif_value_foreign * exchange_rate_cbic, 2)
        bcd = round((assessable_inr * bcd_rate_pct) / 100.0, 2)
        sws = round((bcd * sws_rate_pct) / 100.0, 2)
        taxable_for_igst = assessable_inr + bcd + sws
        igst = round((taxable_for_igst * igst_rate_pct) / 100.0, 2)

        total_duty = round(bcd + sws + igst, 2)
        total_landed = round(assessable_inr + total_duty, 2)

        return CustomsLandedCostAssessment(
            assessable_value_inr=assessable_inr,
            basic_customs_duty_bcd=bcd,
            social_welfare_surcharge_sws=sws,
            integrated_gst_igst=igst,
            total_customs_duty_payable=total_duty,
            total_landed_cost_inr=total_landed
        )

    def calculate_export_incentives(
        self,
        shipping_bill_no: str,
        fob_value_inr: float,
        dbk_rate_pct: float = 2.0,
        rodtep_rate_pct: float = 1.2
    ) -> DutyDrawbackClaim:
        dbk = round((fob_value_inr * dbk_rate_pct) / 100.0, 2)
        rodtep = round((fob_value_inr * rodtep_rate_pct) / 100.0, 2)
        return DutyDrawbackClaim(
            shipping_bill_number=shipping_bill_no,
            fob_value_inr=fob_value_inr,
            drawback_rate_pct=dbk_rate_pct,
            eligible_drawback_inr=dbk,
            rodtep_rate_pct=rodtep_rate_pct,
            eligible_rodtep_inr=rodtep,
            total_export_incentive_inr=round(dbk + rodtep, 2)
        )
