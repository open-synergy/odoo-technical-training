# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


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
        string="Dosen",
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

    @api.onchange(
        "mata_kuliah_id",
        )
    def _onchange_dosen(self):
        self.dosen_id = False
        kriteria = {}
        if self.mata_kuliah_id.dosen_ids:
            self.dosen_id = self.mata_kuliah_id.dosen_ids[0]
            kriteria.update({
                "dosen_id": [
                    ("id", "in", self.mata_kuliah_id.dosen_ids.ids),
                    ],
                })

        return {
            "domain": kriteria,
            }


