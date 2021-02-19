# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class MailMail(models.Model):
    _inherit = 'mail.mail'

    @api.model
    def create(self, vals):
        """From email updated based on Outgoing mail server."""
        res = super(MailMail, self).create(vals)
        if res.model == 'crm.lead':
            outgoing_mail = self.env['ir.mail_server'].sudo().search([('active', '=', True)], limit=1)
            if outgoing_mail:
                res.write({'email_from': outgoing_mail.smtp_user,
                           'reply_to': outgoing_mail.smtp_user})
        return res

