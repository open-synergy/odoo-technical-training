# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class UniversitasDosen(models.Model):
    _name = "universitas.dosen_baru"
    _inherits = {"hr.employee":"employee_id"}
    _inherit = ["mail.thread"]
    _description = "Dosen"
    
    employee_id = fields.Many2one(
        string="Employee",
        comodel_name="hr.employee",
        required=True,
        ondelete="cascade",
        )
    kode_dosen = fields.Char(
        string="Kode Dosen",
        required=True
    )
    mata_kuliah_ids = fields.Many2many(
        string="Mata Kuliah",
        comodel_name="universitas.mata_kuliah",
        relation="rel_mata_kuliah_2_dosen_baru",
        column1="dosen_baru_id",
        column2="mata_kuliah_id",
        )
