# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class UniversitasDosen(models.Model):
    _name = "universitas.dosen"
    _description = "Dosen"
    
    kode_dosen = fields.Char(
        string="Kode Dosen",
        required=True
    )

    name = fields.Char(
        string="Jadwal",
        required=True
    )
    mata_kuliah_ids = fields.Many2many(
        string="Mata Kuliah",
        comodel_name="universitas.mata_kuliah",
        relation="rel_mata_kuliah_2_dosen",
        column1="dosen_id",
        column2="mata_kuliah_id",
        )

