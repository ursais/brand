# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestBrandExternalReportLayout(TransactionCase):
    def setUp(self):
        super(TestBrandExternalReportLayout, self).setUp()
        self.brand = self.env['res.brand'].create({'name': 'brand'})

    def test_change_report_template(self):
        self.brand.change_report_template()
        self.assertEqual(
            self.env.ref(
                'brand_external_report_layout.res_brand_document_template_form'
            ).id,
            self.brand.change_report_template()['view_id'],
        )

    def test_get_logo(self):
        self.assertEqual(self.brand.logo, self.brand._get_logo())