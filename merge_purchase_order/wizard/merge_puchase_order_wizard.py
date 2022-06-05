# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class MergePurchaseOrder(models.TransientModel):
    _name = 'merge.purchase.order'
    _description = 'Merge Purchase Order'

    merge_type = fields.Selection([('new_cancel', 'Create new order and cancel all selected purchase orders'),
                                   ('new_delete', 'Create new order and delete all selected purchase orders'),
                                   ('merge_cancel', 'Merge order on existing selected order and cancel others'),
                                   ('merge_delete', 'Merge order on existing selected order and delete others')],
                                  default='new_cancel')
    purchase_order_id = fields.Many2one('purchase.order', 'Purchase Order')

    @api.onchange('merge_type')
    def onchange_merge_type(self):
        res = {}
        for order in self:
            order.purchase_order_id = False
            if order.merge_type in ['merge_cancel', 'merge_delete']:
                purchase_orders = self.env['purchase.order'].browse(
                    self._context.get('active_ids', []))
                res['domain'] = {
                    'purchase_order_id':
                    [('id', 'in',
                        [purchase.id for purchase in purchase_orders])]
                }
            return res

    def merge_orders(self):
        purchase_orders = self.env['purchase.order'].browse(self._context.get('active_ids', []))
        if len(self._context.get('active_ids', [])) < 2:
            raise UserError(_('Please select atleast two purchase orders to perform the Merge Operation.'))
        if any(order.state != 'draft' for order in purchase_orders):
            raise UserError(_('Please select Purchase orders which are in RFQ state to perform the Merge Operation.'))
        partner = purchase_orders[0].partner_id.id
        if any(order.partner_id.id != partner for order in purchase_orders):
            raise UserError(_('Please select Purchase orders whose Vendors are same to perform the Merge Operation.'))
        if self.merge_type == 'new_cancel':
            purchase_origin = set()
            po = self.env['purchase.order'].with_context({
                'trigger_onchange': True,
                'onchange_fields_to_trigger': [partner]
            }).create({'partner_id': partner})
            default = {'order_id': po.id}
            for order in purchase_orders:
                purchase_origin.add(order.origin)
                for line in order.order_line:
                    line.copy(default=default)
            po.write({
                'origin': ', '.join(purchase_origin)
            })
            for order in purchase_orders:
                order.button_cancel()
        elif self.merge_type == 'new_delete':
            purchase_origin = set()
            po = self.env['purchase.order'].with_context({
                'trigger_onchange': True,
                'onchange_fields_to_trigger': [partner]
            }).create({'partner_id': partner})
            default = {'order_id': po.id}
            for order in purchase_orders:
                purchase_origin.add(order.origin)
                for line in order.order_line:
                    line.copy(default=default)
            po.write({
                'origin': ', '.join(purchase_origin)
            })
            for order in purchase_orders:
                order.sudo().button_cancel()
                order.sudo().unlink()
        elif self.merge_type == 'merge_cancel':
            default = {'order_id': self.purchase_order_id.id}
            po = self.purchase_order_id
            purchase_origin = set(po.origin.split(', '))
            for order in purchase_orders:
                for each in order.origin.split(', '):
	                purchase_origin.add(each)
                if order.id != default['order_id']:
                    for line in order.order_line:
                        line.copy(default=default)
            origin = ', '.join(purchase_origin)
            po.write({
                'origin': origin.strip()
            })
            for order in purchase_orders:
                if order != po:
                    order.sudo().button_cancel()
        else:
            default = {'order_id': self.purchase_order_id.id}
            po = self.purchase_order_id
            purchase_origin = set(po.origin.split(', '))
            for order in purchase_orders:
                for each in order.origin.split(', '):
	                purchase_origin.add(each)
                if order.id != default['order_id']:
                    for line in order.order_line:
                        line.copy(default=default)
            origin = ', '.join(purchase_origin)
            po.write({
                'origin': origin.strip()
            })
            for order in purchase_orders:
                if order != po:
                    order.sudo().button_cancel()
                    order.sudo().unlink()
