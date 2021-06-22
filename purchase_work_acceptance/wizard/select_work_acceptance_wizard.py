# Copyright 2019 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, fields, models
from odoo.exceptions import ValidationError


class SelectWorkAcceptanceWizard(models.TransientModel):
    _name = "select.work.acceptance.wizard"
    _description = "Select Work Acceptance Wizard"

    require_wa = fields.Boolean(default=lambda self: self._get_require_wa())
    wa_id = fields.Many2one(
        comodel_name="work.acceptance",
        string="Work Acceptance",
        domain=lambda self: self._get_wa_domain(),
    )

    def _get_require_wa(self):
        return self.env.user.has_group(
            "purchase_work_acceptance.group_enforce_wa_on_invoice"
        )

    def _get_wa_domain(self):
        wa = self.env["work.acceptance"]._get_valid_wa(
            "invoice", self.env.context.get("active_id")
        )
        return [("id", "in", wa.ids)]

    def button_create_vendor_bill(self):
        self.ensure_one()
        order_id = self._context.get("active_id")
        wa = self.env["work.acceptance"]._get_valid_wa("invoice", order_id)
        if self.wa_id not in wa:
            raise ValidationError(
                _("%s was already used by some bill") % self.wa_id.name
            )
        order = self.env["purchase.order"].browse(order_id)
        return order.with_context(
            create_bill=False, wa_id=self.wa_id.id
        ).action_create_invoice()
