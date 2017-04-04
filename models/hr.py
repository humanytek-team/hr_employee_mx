# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import _


class Employee(models.Model):
    #_name = "hr.employee"
    _inherit = "hr.employee"

    imss = fields.Char("IMSS", help=_("Mexican Social Security Institute"))
