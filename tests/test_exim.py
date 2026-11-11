import unittest
from exim.engine import EximCustomsEngine

class TestEximCustoms(unittest.TestCase):
    def test_assess_import_customs(self):
        engine = EximCustomsEngine()
        assessment = engine.assess_import_customs(
            cif_value_foreign=10000.0,
            exchange_rate_cbic=83.50,
            bcd_rate_pct=10.0,
            sws_rate_pct=10.0,
            igst_rate_pct=18.0
        )
        self.assertEqual(assessment.assessable_value_inr, 835000.0)
        self.assertEqual(assessment.basic_customs_duty_bcd, 83500.0)
        self.assertEqual(assessment.social_welfare_surcharge_sws, 8350.0)
        self.assertEqual(assessment.integrated_gst_igst, 166833.0)
        self.assertEqual(assessment.total_customs_duty_payable, 258683.0)

    def test_export_incentives(self):
        engine = EximCustomsEngine()
        claim = engine.calculate_export_incentives(
            shipping_bill_no="SB-2026-98712",
            fob_value_inr=1500000.0,
            dbk_rate_pct=2.0,
            rodtep_rate_pct=1.5
        )
        self.assertEqual(claim.eligible_drawback_inr, 30000.0)
        self.assertEqual(claim.eligible_rodtep_inr, 22500.0)
        self.assertEqual(claim.total_export_incentive_inr, 52500.0)

if __name__ == "__main__":
    unittest.main()
