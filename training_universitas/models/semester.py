# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.exceptions import Warning as UserError


class UniversitasSemester(models.Model):
    _name = "universitas.semester"
    _description = "Semester"
    _order = "date_start desc"

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
        copy=False,
    )

    date_end = fields.Date(
        string="Date End",
        copy=False,
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
    registrasi_sequence_id = fields.Many2one(
        string="Registrasi Sequence",
        comodel_name="ir.sequence",
        )

    @api.constrains(
        "date_start", "date_end",
        )
    def _check_date(self):
        if self.date_start >= self.date_end and \
                self.date_start and \
                self.date_end:
            raise UserError("Tanggal mulai harus lebih kecil dari tanggal selesai")


