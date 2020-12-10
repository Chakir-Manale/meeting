# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Meeting",
			"category": "Modules",
			"color": "black",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Meeting Management")
		
		},
		{
			"module_name": "Chantiers",
			"category": "Modules",
			"color": "black",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Chantiers")
		}

	]