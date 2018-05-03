# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class UniversitasRegistrasi(models.Model):
    _name = "universitas.registrasi"
    _description = "Registrasi"

    name = fields.Char(
        string="# Registrasi",
        required=True,
    )
    mahasiswa_id = fields.Many2one(
        string="Mahasiswa",
        comodel_name="universitas.mahasiswa"
    )
    semester_id =  fields.Many2one(
        string="Semester",
        comodel_name="universitas.semester"
    )
    amount_total = fields.Float(
        string="Amount Total",
        digits=(16,3),
    )
    total_sks = fields.Float(
        string="Total SKS",
        )
    detail_ids = fields.One2many(
        string="Detail",
        comodel_name="universitas.registrasi_detail",
        inverse_name="registrasi_id",
    )
