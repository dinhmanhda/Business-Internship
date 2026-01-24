# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class qltc__kt(models.Model):
#     _name = 'qltc__kt.qltc__kt'
#     _description = 'qltc__kt.qltc__kt'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
