# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class UniversitasRegistrasiDetail(models.Model):
    _name = "universitas.registrasi_detail"
    _description = "Registrasi Detail"

    mata_kuliah_id = fields.Many2one(
        string="Mata Kuliah",
        comodel_name="universitas.mata_kuliah",
        domain=[
            ("sks",">",0),
            ],
        )
    sks = fields.Integer(
        string="SKS",
        related="mata_kuliah_id.sks",
        store=True,
        readonly=True,
        )
    price_unit = fields.Float(
        string="Amount Total",
    )
    price_subtotal = fields.Float(
        string="Price Subtotal",
    )
    registrasi_id = fields.Many2one(
        string="Registrasi",
        comodel_name="universitas.registrasi",
        on_delete="cascade",
    )    
