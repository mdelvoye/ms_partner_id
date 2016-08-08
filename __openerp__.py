# -*- coding: utf-8 -*-
{
    "name" : "MS Partner Id",
    "version" : "9.0.1.0",
    "category" : "Base",
    'author': u'Misyl Services',
    'depends' : ['base','ms_core'],
    "data" : [
              'views/res_partner_view.xml',
              'views/ms_partner_id.xml',              
             ],
    'installable': True,
    'auto_install': False,
    'sequence' : 15
}
