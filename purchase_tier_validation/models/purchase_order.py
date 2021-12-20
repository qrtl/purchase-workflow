# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _name = "purchase.order"
    _inherit = ['purchase.order', 'tier.validation']
    _state_from = ['draft', 'sent']
    _state_to = ['purchase', 'approved']

    is_reviewer = fields.Boolean(default=False, compute="_compute_is_reviewer")

    @api.multi
    def _compute_is_reviewer(self):
        #uid = self.env.uid
        for order_line in self:
            order_line.is_reviewer = False
            # for tier in order_line.review_ids:
            #     if uid in tier.reviewer_ids:
            #         order_line.is_reviewer = True
            #         break
    # when access to each record of sale_order (select order or create order), error below occured.
    '''
    Odoo Odoo Client Error
    Uncaught Error: Unknown field is_reviewer in domain ["|",["review_ids","=",[]],["is_reviewer","=",false]]
    https://dev3.quartile.co/web/content/10875-eb826f4/web.assets_backend.js:1767
    Traceback:
    Error: Unknown field is_reviewer in domain ["|",["review_ids","=",[]],["is_reviewer","=",false]]
        at Object.compute_domain (https://dev3.quartile.co/web/content/10875-eb826f4/web.assets_backend.js:1767:42)
        at Class.compute_domain (https://dev3.quartile.co/web/content/10875-eb826f4/web.assets_backend.js:2190:344)
        at Class.<anonymous> (https://dev3.quartile.co/web/content/10875-eb826f4/web.assets_backend.js:2224:364)
        at Class.trigger (https://dev3.quartile.co/web/content/10861-2c6b16c/web.assets_common.js:3105:180)
        at Class.trigger (https://dev3.quartile.co/web/content/10861-2c6b16c/web.assets_common.js:3109:148)
        at Class.on_form_changed (https://dev3.quartile.co/web/content/10875-eb826f4/web.assets_backend.js:2140:98)
        at Array.<anonymous> (https://dev3.quartile.co/web/content/10875-eb826f4/web.assets_backend.js:2137:6)
        at Array.<anonymous> (https://dev3.quartile.co/web/content/10861-2c6b16c/web.assets_common.js:547:681)
        at fire (https://dev3.quartile.co/web/content/10861-2c6b16c/web.assets_common.js:541:299)
        at Object.add [as done] (https://dev3.quartile.co/web/content/10861-2c6b16c/web.assets_common.js:542:467)
    '''
