# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model_create_multi
    def create(self, vals_list):
        moves = super(AccountMove, self).create(vals_list)
        for move in moves:
            _logger.debug("Iniciando proceso de creación de factura %s", move.name)

            # Buscar el pedido de venta asociado
            sale_order = self.env['sale.order'].search([('name', '=', move.invoice_origin)], limit=1)

            if not sale_order:
                _logger.warning("No se encontró el pedido de venta asociado con el número %s", move.invoice_origin)
                continue

            # Verificar si el pedido de venta tiene un número origin
            if not sale_order.origin:
                _logger.warning("El pedido de venta %s no tiene un valor origin configurado", sale_order.name)
                continue

            # Crear la referencia de documento
            try:
                # Buscar el tipo de documento 801 por código
                doc_type_801 = self.env['l10n_latam.document.type'].search([('code', '=', '801')], limit=1)
                if not doc_type_801:
                    _logger.error("No se pudo encontrar el tipo de documento con código 801")
                    continue

                reference_vals = {
                    'origin_doc_number': sale_order.origin,
                    'date': sale_order.date_order.date(),
                    'l10n_cl_reference_doc_type_id': doc_type_801.id,
                    'move_id': move.id,
                }

                # Crear la referencia de documento
                self.env['l10n_cl.account.invoice.reference'].create(reference_vals)
                _logger.debug("Referencia de documento creada exitosamente")

            except Exception as e:
                _logger.error("Error al crear la referencia de documento: %s", str(e))

        return moves
