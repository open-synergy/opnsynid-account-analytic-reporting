# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrTimesheetReport(models.Model):
    _inherit = "hr.timesheet.report"

    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
    )
    other_partner_id = fields.Many2one(
        string="Other Partner",
        comodel_name="res.partner",
    )

    def _select(self):
        str_select = super(HrTimesheetReport, self)._select()
        str_select += """
            ,
            hat.partner_id AS partner_id,
            hat.other_partner_id AS other_partner_id
            """
        return str_select

    def _group_by(self):
        group_by_str = super(HrTimesheetReport, self)._group_by()
        group_by_str += """
            ,
            hat.partner_id,
            hat.other_partner_id
            """
        return group_by_str
