# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class UniversitasAbsen(models.Model):
    _name = "universitas.absen"
    _description = "Absen"

    jadwal_id = fields.Many2one(
        string="Jadwal",
        required=True,
    )

    registrasi_detail_id = fields.Many2one(
        string="Registrasi Detail",
        comodel_name="universitas.registrasi_detail",
        required=True
    )
    
    state = fields.Selection(
        string="State",
        selection=[
            ("hadir", "Hrdie"),
            ("izin", "Izin"),
            ("absen", "Absen")
        ],
        default="absen",
    )

