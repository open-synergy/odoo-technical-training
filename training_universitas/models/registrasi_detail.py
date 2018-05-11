# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class UniversitasRegistrasiDetail(models.Model):
    _name = "universitas.registrasi_detail"
    _description = "Registrasi Detail"

    @api.multi
    @api.depends(
        "sks", "price_unit",
        )
    def _compute_price(self):
        for detail in self:
            detail.price_subtotal = detail.sks * \
                detail.price_unit

    mata_kuliah_id = fields.Many2one(
        string="Mata Kuliah",
        comodel_name="universitas.mata_kuliah",
        domain=[
            ("sks",">",0),
            ],
        )
    sks = fields.Integer(
        string="SKS",
        )
    price_unit = fields.Float(
        string="Price",
    )
    pricelist_id = fields.Many2one(
        string="Pricelist",
        comodel_name="product.pricelist",
        )
    price_subtotal = fields.Float(
        string="Price Subtotal",
        compute="_compute_price",
    )
    registrasi_id = fields.Many2one(
        string="Registrasi",
        comodel_name="universitas.registrasi",
    )    
