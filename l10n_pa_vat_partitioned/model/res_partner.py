# !/usr/bin/python
# -*- encoding: utf-8 -*-
#
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2014 Vauxoo - http://www.vauxoo.com/
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
#
#    Coded by: vauxoo consultores (info@vauxoo.com)
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from openerp import models, fields, api


class ResPartner(models.Model):

    # Will be part of res.partner model
    _inherit = "res.partner"

    def get_panama_code(self):
        panama = None
        for panama_id in self.env['res.country'].search(
                [('name', '=', 'Panama')]):
            panama = panama_id
        return panama

    @api.onchange('l10n_pa_ruc', 'l10n_pa_ruc_dv')
    def _onchange_partitioned_vat(self):
        if self.l10n_pa_ruc:
            self.vat = "PA%s" % self.l10n_pa_ruc
        if self.l10n_pa_ruc and self.l10n_pa_ruc_dv:
            self.vat = "PA%sDV%s" % (self.l10n_pa_ruc, self.l10n_pa_ruc_dv)

    # COLUMNS
    l10n_pa_ruc_country_id = fields.Many2one(
        'res.country', ondelete="set null", default=get_panama_code)
    l10n_pa_ruc = fields.Char(
        string="RUC", size=25)
    l10n_pa_ruc_dv = fields.Char(
        string="DV", size=2)
