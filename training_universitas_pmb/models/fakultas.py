# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class UniversitasFakultas(models.Model):
    _inherit = "universitas.fakultas"

    pricelist_id = fields.Many2one(
        string="Pricelist Formulir Pendaftaran",
        comodel_name="product.pricelist",
        )
