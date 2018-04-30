# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class UniversitasFakultas(models.Model):
    _name = "universitas.fakultas"
    _description = "Fakultas"

    name = fields.Char(
        string="Fakultas",
        required=True,
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
