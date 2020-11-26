from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Meeting"),
			"items": [
				{
					"type": "doctype",
					"name": "Meeting",
					"description": _("Meeting doctype ."),
					"onboard": 1,
				}
			]
		},
	]