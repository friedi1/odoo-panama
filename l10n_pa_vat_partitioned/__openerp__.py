#!/usr/bin/python
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
#
#

{
    "name": "Partitioned VAT",
    "version": "1.0",
    "author": "Vauxoo",
    "category": "Generic Modules",
    "description": """
        l10n_pa_vat_partitioned

        This module splits the VAT field into 3 fields:
            1. l10n_pa_ruc_country_id (PA)
            2. l10n_pa_ruc (RUC)
            3. l10n_pa_ruc_dv (DV)

        The previous fields will be disposed to replace the directly
        'VAT' field editing.
    """,
    "website": "http://www.vauxoo.com/",
    "license": "AGPL-3",
    "depends": [
        "base",
        "account",
        "l10n_pa_vat",
    ],
    "demo": [],
    "data": [
        "view/res_partner_view.xml",
    ],
    "test": [],
    "installable": True,
    "active": False,
}
