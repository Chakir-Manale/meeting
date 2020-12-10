from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("liste des chantiers"),
			"items": 
            [
				{
					"type": "doctype",
					"name": "Chantier",
					"description": _("Chantier doctype ."),
					"onboard": 1,
				}
			]
		},
    ]