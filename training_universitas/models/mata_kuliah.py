# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class UniversitasMataKuliah(models.Model):
    _name = "universitas.mata_kuliah"
    _description = "Mata Kuliah"
    _sql_constraints = [
        ('unique_kode', 'unique (kode)', 'Kode tidak boleh sama'),
        ]

    name = fields.Char(
        string="Mata Kuliah",
        required=True,
        translate=True,
    )

    kode = fields.Char(
        string="Kode",
        required=True,
    )

    active = fields.Boolean(
        string="Active",
        default=True,
    )

    sks = fields.Integer(
        string="SKS",
    )

    keterangan = fields.Text(
        string="Keterangan",
    )

    aktivitas_mk_ids = fields.Many2many(
        string="Aktivitas Mata Kuliah",
        comodel_name="universitas.aktivitas_mk",
        relation="rel_matakuliah_2_aktivitas",
        column1="mata_kuliah_id",
        column2="aktivitas_id",
    )
