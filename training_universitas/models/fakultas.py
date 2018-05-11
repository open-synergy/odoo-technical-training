# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, tools


class UniversitasFakultas(models.Model):
    _name = "universitas.fakultas"
    _inherits = {"hr.department":"department_id"}
    _description = "Fakultas"

    @api.multi
    def _compute_image(self):
        for fak in self:
            fak.image_small = tools.image_get_resized_images(fak.image, return_small=True, small_name="image_small")["image_small"]
            fak.image_medium = tools.image_get_resized_images(fak.image, return_medium=True, medium_name="image_medium")["image_medium"]
            fak.image_big = tools.image_get_resized_images(fak.image, return_big=True, big_name="image_big")["image_big"]



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
    image_small = fields.Binary(
        string="Image Small",
        compute="_compute_image",
    )
    image_medium = fields.Binary(
        string="Image Medium",
        compute="_compute_image",
    )
    image_big = fields.Binary(
        string="Image",
        compute="_compute_image",
    )
