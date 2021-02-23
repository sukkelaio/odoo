# -*- encoding: utf-8 -*-

{
    'name': 'CRM: Outgoing Mail',
    'version': '14.0.1.2.0',
    'sequence': 1,
    'category': 'Mail',
     'summary': 'Set "From" email address in outgoing email to be the same as your outgoing email server email address.',
    'description': '''
CRM: Outgoing Mail
======================
* Forces the "From" email address to be the same as your outgoing email.
    ''',
    'depends': ['mail'],
    'author': "sukkela.io<info@sukkela.io>",
    'website': "https://sukkela.io",
    'license': 'OPL-1',
    'data': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/sukkela_200_high_rounded.png'],
}
