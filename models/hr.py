# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import _


class Employee(models.Model):
    _inherit = "hr.employee"

    imss = fields.Char("IMSS", help=_("Mexican Social Security Institute"))
    rfc = fields.Char("RFC", help=_("Federal Taxpayer Registration"))
