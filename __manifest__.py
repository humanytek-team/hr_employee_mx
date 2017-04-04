# -*- coding: utf-8 -*-
{
    'name': "l10n_mx_employee",
    'summary': """
        Adds some fields to the model hr.employee required by Mexican laws""",
    'description': """
        Adds some fields to the model hr.employee required by Mexican laws
    """,
    'author': "Humanytek",
    'website': "http://humanytek.com",
    'category': 'Human Resources',
    'version': '0.1',
    'depends': ['base', 'hr'],
    'data': [
        'views/views.xml',
    ],
}
