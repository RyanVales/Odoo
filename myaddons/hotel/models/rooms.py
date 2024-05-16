# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rooms(models.Model):
    _name = 'hotel.rooms'
    _description = 'Hotel Rooms'
    _order = 'name'

    name = fields.Char("Room Names")
    description = fields.Char("Room Description")
    roomtype_id = fields.Many2one('hotel.roomtypes', string="Roomtype")
    roomtypename = fields.Char("Room Type",related='roomtype_id.name')
