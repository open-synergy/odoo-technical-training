# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class UniversitasKelas(models.Model):
    _name = "universitas.kelas"
    _description = "Kelas"

    name = fields.Char(
        string="Kelas",
        required=True,
    )

    semester_id = fields.Many2one(
        string="Semester",
        comodel_name="universitas.semester",
        required=True
    )

    mata_kuliah_id = fields.Many2one(
        string="Mata Kuliah",
        comodel_name="universitas.mata_kuliah",
        required=True
    )
    
    dosen_id = fields.Many2one(
        string="Kelas",
        comodel_name="universitas.dosen",
        required=True
    )

    keterangan = fields.Text(
        string="Keterangan"
    )

    active = fields.Boolean(
        string="Active",
        default=True
    )
