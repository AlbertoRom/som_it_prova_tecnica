import json

from odoo import http
from odoo.http import request


class ConsumptionController(http.Controller):
    _name = 'consumption.controller'

    @http.route('/api/cosnumptions', type='http',
                auth='public', methods=['GET'], csrf=False)
    def index(self, **kv):
        consumptions = [
            {
                'id': consumption.id,
                'product': consumption.product_id.name,
                'date': str(consumption.date),
                'quantity': consumption.quantity,
            }
            for consumption in request.env['consumption'].sudo().search([])
        ]
        return request.make_response(
            json.dumps({'Consumptions': consumptions}),
            [('Content-Type', 'application/json')]
        )

    @http.route('/api/cosnumption/<int:consumption_id>', type='http',
                auth='public', methods=['GET'], csrf=False)
    def show(self, consumption_id, **kv):
        consumption = request.env['consumption'].sudo().search([
            ('id', '=', consumption_id)
        ])
        data = {
            'id': consumption.id,
            'product': consumption.product_id.name,
            'date': str(consumption.date),
            'quantity': consumption.quantity,
        }
        return request.make_response(
            json.dumps({'Consumption': data}),
            [('Content-Type', 'application/json')]
        )

    @http.route('/api/cosnumption', type='http',
                auth='public', methods=['POST'], csrf=False)
    def create(self, **kv):
        data = json.loads(request.httprequest.data)
        product_template = request.env['product.template'].sudo().search([
            ('default_code', '=', data['code'])
        ])
        del data['code']
        data['product_id'] = product_template.id
        new_consumption = request.env['consumption'].sudo().create(data)
        data = {
            'id': new_consumption.id,
            'name': new_consumption.product_id.name,
            'date': str(new_consumption.date),
            'quantity': new_consumption.quantity,
        }
        return request.make_response(
            json.dumps({'Consumption': data}),
            [('Content-Type', 'application/json')]
        )

    @http.route('/api/cosnumption/<int:consumption_id>', type='http',
                auth='public', methods=['PUT'], csrf=False)
    def update(self, consumption_id, **kv):
        consumption = request.env['consumption'].sudo().search([
            ('id', '=', consumption_id)
        ])
        data = json.loads(request.httprequest.data)
        product_template = request.env['product.template'].sudo().search([
            ('default_code', '=', data['code'])
        ])
        del data['code']
        data['product_id'] = product_template.id
        consumption.write(data)
        data = {
            'id': consumption.id,
            'name': consumption.product_id.name,
            'date': str(consumption.date),
            'quantity': consumption.quantity,
        }
        return request.make_response(
            json.dumps({'Consumption': data}),
            [('Content-Type', 'application/json')]
        )

    @http.route('/api/cosnumption/<int:consumption_id>', type='http',
                auth='public', methods=['DELETE'], csrf=False)
    def delete(self, consumption_id, **kv):
        consumption = request.env['consumption'].sudo().search([
            ('id', '=', consumption_id)
        ])
        data = {
            'id': consumption.id,
            'name': consumption.product_id.name,
            'date': str(consumption.date),
            'quantity': consumption.quantity,
        }
        consumption.unlink()
        return request.make_response(
            json.dumps({'Consumption': data}),
            [('Content-Type', 'application/json')]
        )
