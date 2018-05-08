# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.exceptions import Warning as UserError


class UniversitasMahasiswa(models.Model):
    _name = "universitas.mahasiswa"
    _description = "Mahasiswa"

    nim = fields.Char(
        string="NIM",
        required=True,
        default="/",
        copy=False,
    )
    name = fields.Char(
        string="Name",
        required=True
    )
    program_studi_id = fields.Many2one(
        string="Program Studi",
        comodel_name="universitas.program_studi",
        )
    fakultas_id = fields.Many2one(
        string="Fakultas",
        comodel_name="universitas.fakultas",
        related="program_studi_id.fakultas_id",
        store=True,
        )

    @api.model
    def create(self, values):
        # raise UserError(str(values))
        nim = values.get("nim", False)
        program_studi_id = values.get("program_studi_id", False)
        if not nim or nim == "/":
                prodi = self.env["universitas.program_studi"].\
                    browse([program_studi_id])[0]
                values["nim"] = self.env["ir.sequence"].\
                    next_by_id(prodi.nim_sequence_id.id)
        return super(UniversitasMahasiswa, self).create(values)

    @api.multi
    def copy(self, values):
        raise UserError("No Copy")
