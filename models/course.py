from odoo import fields, models


class Courses(models.Model):
    _name = "citadel.courses"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "course table"

    name=fields.Char(string='Name:', required=True)
    time1 = fields.Char(string='time')
    mail= fields.Char(string='Mail-id:', required=True)
    phone = fields.Char(string='Phone no:', size=10, required=True)
    sessions = fields.Many2many('citadel.sessions',
                                  'sessions_time_rel',
                                  'sessions_id',
                                  'time_id', string='Select Session', required=True)
    image = fields.Binary(string='image')

class Sessions(models.Model):
    _name = "citadel.sessions"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "session table"

    session1 = fields.Char(string='Session')
    level = fields.Selection([('beginner','Beginner'),('intermediate','Intermediate'),('expert','Expert')],string='Level')
    time2 = fields.Char(string='Time')
    maester = fields.Char(string='Maester name:')
