# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class UniversitasFakultas(models.Model):
    _name = "universitas.fakultas"
    _inherits = {"hr.department":"department_id"}
    _description = "Fakultas"

    department_id = fields.Many2one(
        string="Department",
        comodel_name="hr.department",
        required=True,
        ondelete="cascade",
        )
    kode = fields.Char(
        string="Kode",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )

    keterangan = fields.Text(
        string="Keterangan",
    )

    image = fields.Binary(
        string="Image"
    )
