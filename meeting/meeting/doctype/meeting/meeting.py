# -*- coding: utf-8 -*-
# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class Meeting(Document):
    pass
    """def validate(self):
		 set missing names 
		for attendee in self.attendees:
			if not attendee.full_name:
				attendee.full_name = get_full_name(attendee.attendee)		
		"""


@frappe.whitelist()
def get_full_name(attendee):
    """
    -- function that returns user full name when a user is selected 
                    in the attendees section in new meeting form -- 

            frappee.get_doc(doctype,name) 
                    => Returns a Document object of the record identified by doctype and name
            attendee.attendee === meeting.meeting_attendee.attendee
    """
    user = frappe.get_doc("User", attendee)

    # Concatenate by space if has value
    return " ".join(filter(None, [user.first_name, user.last_name]))
    #attendee.full_name = user.full_name
