# -*- coding: utf-8 -*-

from odoo import models, fields, api


class guests(models.Model):
    _name = 'hotel.guests'
    _description = 'Hotel Guests'
    _order='lastname,firstname,middlename'

    name = fields.Char("Guest Name")
    description = fields.Char("Charge Description")
    lastname = fields.Char("Last Name")
    firstname = fields.Char("First Name")
    middlename = fields.Char("Middle Name")
    address_streetno = fields.Char("Street & No.")
    address_area = fields.Char("Area,Unit and Bldg,Barangay")
    address_city = fields.Char("City / Town")
    address_province = fields.Char("Province / State")
    contactno = fields.Char("Contact Number")
    zipcode = fields.Char("Zip Code")
    gender = fields.Selection([('FEMALE','Female'),('MALE','Male')],string="Gender")
    birthdate = fields.Date("Birthdate")
    photo = fields.Image(string="Guest Photo")
    name = fields.Char(string='Guest Name', compute='_compute_name')
    
    @api.depends('lastname','firstname','middlename')
    def _compute_name(self):
        for rec in self:
            rec.name=f"{rec.lastname}, {rec.firstname} {rec.middlename}"
    
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
    
