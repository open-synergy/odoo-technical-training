# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class UniversitasProgramStudi(models.Model):
    _name = "universitas.program_studi"
    _description = "Program Studi"

    name = fields.Char(
        string="Program Studi",
        required=True,
        help="Ini adalah nama Program Studi"
    )

    kode = fields.Char(
        string="Kode",
        required=True,
    )

    active = fields.Boolean(
        string="Active",
        default=True,
    )

    keterangan = fields.Text(
        string="Keterangan",
    )

    fakultas_id = fields.Many2one(
        string="Fakultas",
        comodel_name="universitas.fakultas",
        ondelete="restrict",
    )    
