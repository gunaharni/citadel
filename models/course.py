from odoo import api, fields, models


class Courses(models.Model):
    _name = "citadel.courses"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "course table"

    name = fields.Char(string='Name', required=True)
    level = fields.Selection(
        string='Difficulty',
        selection=[
            ('easy', 'Easy'),
            ('medium', 'Medium'),
            ('hard', 'Hard'),
        ],
        default='medium')
    instructor = fields.Many2one(string='Instructor', comodel_name='res.partner', requried=True)
    description = fields.Text(string='Description')
    session_ids = fields.One2many(comodel_name='citadel.sessions', inverse_name='course_id')
    session_count = fields.Integer(string='No. of Sessions', compute='_compute_session_count', store=True)

    @api.depends('session_ids')
    def _compute_session_count(self):
        for record in self:
            record.session_count = len(record.session_ids)

    @api.onchange('level')
    def change_description(self):
        for record in self:
            if record.level == 'hard':
                record.description = '[Hard] ' + str(record.description)
