# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class UniversitasMahasisa(models.Model):
    _name = "universitas.mahasiswa"
    _description = "Mahasiswa"

    nim = fields.Char(
        string="NIM",
        required=True
    )

    name = fields.Char(
        string="Jadwal",
        required=True
    )

