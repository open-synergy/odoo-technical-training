# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class UniversitasJadwal(models.Model):
    _name = "universitas.jadwal"
    _description = "Jadwal"

    kelas_id = fields.Many2one(
        string="Kelas",
        required=True,
        comodel_name="universitas.kelas",
    )

    date_start = fields.Datetime(
        string="Tanggal Mulai",
        required=True
    )

    date_end = fields.Datetime(
        string="Tanggal Akhir",
        required=True
    )

    keterangan = fields.Text(
        string="Keterangan"
    )

    active = fields.Boolean(
        string="Active",
        default=True
    )

    @api.multi
    def name_get(self):
        result = []
        for jadwal in self:
            name = "%s %s S.D. %s" % (jadwal.kelas_id.name, jadwal.date_start, jadwal.date_end)
            result.append((jadwal.id, name))
        return result

