from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Session(models.Model):
    _name = "citadel.sessions"
    _description = "session table"

    name = fields.Char(string='Title', required=True)
    instructor = fields.Many2one(string='Instructor', comodel_name='res.partner')

    start_date = fields.Datetime(string='Start Date', required=True)
    duration = fields.Float(string='Duration', requried=True, default=1.0, digits=(3, 2), help='Duration (hours)')

    course_id = fields.Many2one(comodel_name='citadel.courses', requried=True)
    course_name = fields.Char(string='Course Name', related='course_id.name')

    state = fields.Selection(
        string='State',
        selection=[
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('done', 'Done'),
        ],
        default='draft')

    attendee_ids = fields.Many2many(string='Attendees', comodel_name='res.partner')
    attendee_count = fields.Integer(string='No. of Attendees', compute='_compute_attendee_count')

    active = fields.Boolean(string='Is Active', default=True)

    @api.constrains('duration')
    def _check_duration(self):
        for record in self:
            if record.duration > 2:
                raise ValidationError(
                    "Session cannot be longer than 2 hours (current value: {})".format(record.duration))

    @api.depends('attendee_ids')
    def _compute_attendee_count(self):
        for record in self:
            record.attendee_count = len(record.attendee_ids)

    def action_confirm(self):
        self.state = 'confirmed'

    def action_draft(self):
        self.state = 'draft'

    def action_done(self):
        self.state = 'done'