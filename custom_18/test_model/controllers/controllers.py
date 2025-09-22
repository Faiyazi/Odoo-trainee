# -*- coding: utf-8 -*-
# from odoo import http


# class TestModel(http.Controller):
#     @http.route('/test_model/test_model', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_model/test_model/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_model.listing', {
#             'root': '/test_model/test_model',
#             'objects': http.request.env['test_model.test_model'].search([]),
#         })

#     @http.route('/test_model/test_model/objects/<model("test_model.test_model"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_model.object', {
#             'object': obj
#         })

