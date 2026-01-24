# -*- coding: utf-8 -*-
# from odoo import http


# class QltcKt(http.Controller):
#     @http.route('/qltc__kt/qltc__kt', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qltc__kt/qltc__kt/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('qltc__kt.listing', {
#             'root': '/qltc__kt/qltc__kt',
#             'objects': http.request.env['qltc__kt.qltc__kt'].search([]),
#         })

#     @http.route('/qltc__kt/qltc__kt/objects/<model("qltc__kt.qltc__kt"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qltc__kt.object', {
#             'object': obj
#         })
