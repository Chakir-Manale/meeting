# -*- coding: utf-8 -*-
# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import dxfgrabber


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


@frappe.whitelist()
def dxfparsing():
    # test dxf parsing
    cwd = 'C:\\Users\\IPS\\Desktop\\win32com\\extractText'
    f = "DCE RSS 16-09-2020.dxf"
    f = r'/home/manale/frappe-bench/apps/meeting/Plan du R+2.dxf'
    frappe.msgprint(f)

    dxf = dxfgrabber.readfile(f)
    print("DXF version: {}".format(dxf.dxfversion))
    layer_count = len(dxf.layers)  # collection of layer definitions

    block_definition_count = len(dxf.blocks)
    entity_count = len(dxf.entities)  # list like collection of entities
    for entity in dxf.entities:
        print(entity.dxftype)
        if hasattr(entity, 'name'):
            frappe.msgprint(entity.name)
        else:
            frappe.msgprint('-------')
