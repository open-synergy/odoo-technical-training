# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class UniversitasAktivitasMataKuliah(models.Model):
    _name = "universitas.aktivitas_mk"
    _description = "Aktivitas Mata Kuliah"

    name = fields.Char(
        string="Aktivitas Mata Kuliah",
        required=True,
    )
    code = fields.Char(
        string="Kode",
    )
    note = fields.Text(
        string="Notes",
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
