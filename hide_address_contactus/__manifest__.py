# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hide Address Contactus',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Hide the company description in contact us',
    'depends': ['website'],
    'data': [
        #'security/ir.model.access.csv',
        # 'data/data.xml',
        'views/company_description.xml',
        #'views/nursery_orders_views.xml',
        #'views/nursery_customers_views.xml',
        #'reports/report.xml',
        #'reports/report_plant_order.xml',
    ],
    'demo': [
        # 'data/demo.xml',
    ],
    # 'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}