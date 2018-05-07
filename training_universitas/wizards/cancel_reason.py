# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class UniversitasRegistrasiCancelReason(models.TransientModel):
    _name = "universitas.registrasi_cancel_reason"
    _description = "Registrasi Cancel Reason"

    cancel_reason = fields.Text(
        string="Cancel Reason",
        required=True,
        )

    @api.multi
    def action_confirm(self):
        self.ensure_one()
        registrasi_id = self._context.get("active_id", False)
        registrasi = self.env["universitas.registrasi"].browse([registrasi_id])[0]
        registrasi.write({
            "cancel_reason": self.cancel_reason,
            })
        registrasi.button_cancel()

