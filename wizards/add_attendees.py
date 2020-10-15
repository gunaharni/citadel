from odoo import api, exceptions, fields, models
from odoo.exceptions import ValidationError


class AddAttendees(models.TransientModel):
    _name = 'citadel.add_attendees'
    _description = 'Wizard to add attendees to a session'

    session_id = fields.Many2one('citadel.sessions', string="Sessions",
                                 default=lambda self: self._context.get('active_id'))
    attendee_ids = fields.Many2many('res.partner', string="Attendees")



    def subscribe(self):
        self.ensure_one()
        for session in self.session_id:
            session.attendee_ids |= self.attendee_ids
        return {}
