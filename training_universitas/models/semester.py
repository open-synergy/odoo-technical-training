# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class UniversitasSemester(models.Model):
    _name = "universitas.semester"
    _description = "Semester"

    name = fields.Char(
        string="Semester",
        required=True,
    )

    kode = fields.Char(
        string="Kode",
        required=True
    )

    date_start = fields.Date(
        string="Date Start",
    )

    date_end = fields.Date(
        string="Date End",
    )

    semester_type = fields.Selection(
        string="Type",
        selection=[
            ("genap", "Genap"),
            ("ganjil", "Ganjil"),
            ("sp", "SP")
        ],
        required=True,
    )

    note = fields.Text(
        string="Notes"
    )

    active = fields.Boolean(
        string="Active",
        default=True
    )