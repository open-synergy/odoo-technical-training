# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class UniversitasRegistrasi(models.Model):
    _name = "universitas.registrasi"
    _description = "Registrasi"

    @api.multi
    @api.depends(
        "detail_ids",
        "detail_ids.sks",
        )
    def _compute_sks(self):
        for registrasi in self:
            registrasi.total_sks = 0
            for detail in registrasi.detail_ids:
                registrasi.total_sks +=  detail.sks

    name = fields.Char(
        string="# Registrasi",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
                ],
            },
    )
    mahasiswa_id = fields.Many2one(
        string="Mahasiswa",
        comodel_name="universitas.mahasiswa",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
                ],
            },

    )
    program_studi_id = fields.Many2one(
        string="Program Studi",
        comodel_name="universitas.program_studi",
        related="mahasiswa_id.program_studi_id",
        store=True,
        readonly=True,
        )
    fakultas_id = fields.Many2one(
        string="Fakultas",
        comodel_name="universitas.fakultas",
        related="mahasiswa_id.fakultas_id",
        store=True,
        readonly=True,
        )
    semester_id =  fields.Many2one(
        string="Semester",
        comodel_name="universitas.semester",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
                ],
            },
    )
    amount_total = fields.Float(
        string="Amount Total",
        digits=(16,3),
    )
    total_sks = fields.Float(
        string="Total SKS",
        compute="_compute_sks",
        )
    detail_ids = fields.One2many(
        string="Detail",
        comodel_name="universitas.registrasi_detail",
        inverse_name="registrasi_id",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
                ],
            },
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("approve", "Approve"),
            ("cancel", "Cancel"),
            ],
        required=True,
        default="draft",
        readonly=True,
        )
    cancel_reason = fields.Text(
        string="Cancel Reason",
        readonly=True,
        )

    @api.multi
    def button_confirm(self):
        for registrasi in self:
            registrasi.write({"state": "confirm"})

    @api.multi
    def button_approve(self):
        for registrasi in self:
            registrasi.write({"state": "approve"})

    @api.multi
    def button_cancel(self):
        for registrasi in self:
            registrasi.write({"state": "cancel"})

    @api.multi
    def button_restart(self):
        for registrasi in self:
            registrasi.write({"state": "draft"})


