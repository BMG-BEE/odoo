# -*- coding: utf-8 -*-

{
    'name': 'HR - Equipments',
    'version': '1.0',
    'sequence': 125,
    'description': """
        Bridge between HR and Maintenance.""",
    'depends': ['hr', 'maintenance'],
    'summary': 'Equipments, Assets, Internal Hardware, Allocation Tracking',
    'data': [
        'views/maintenance_views.xml',
    ],
    'demo': [],
    'installable': True,
    'auto-install': True,
}
