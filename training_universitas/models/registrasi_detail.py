# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class UniversitasRegistrasiDetail(models.Model):
    _name = "universitas.registrasi_detail"
    _description = "Registrasi Detail"

    price_unit = fields.Float(
        string="Amount Total",
    )

    price_subtotal = fields.Float(
        string="Price Subtotal",
    )

    registrasi_id = fields.Many2one(
        string="Registrasi",
        comodel_name="universitas.registrasi",
    )    