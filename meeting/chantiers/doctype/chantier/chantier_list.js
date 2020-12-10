frappe.listview_settings['Chantier'] = {
	
	hide_name_column: true,
	get_indicator: function(doc) {
        return [__(doc.status),{
			"Open": "blue",
			"Closed": "orange",
		}[doc.status], "status,=," + doc.status];
    },
    
};


/*
let imports_in_progress = [];

frappe.listview_settings['Data Import'] = {
	onload(listview) {
		frappe.realtime.on('data_import_progress', data => {
			if (!imports_in_progress.includes(data.data_import)) {
				imports_in_progress.push(data.data_import);
			}
		});
		frappe.realtime.on('data_import_refresh', data => {
			imports_in_progress = imports_in_progress.filter(
				d => d !== data.data_import
			);
			listview.refresh();
		});
	},
	get_indicator: function(doc) {
		var colors = {
			'Pending': 'orange',
			'Not Started': 'orange',
			'Partial Success': 'orange',
			'Success': 'green',
			'In Progress': 'orange',
			'Error': 'red'
		};
		let status = doc.status;
		if (imports_in_progress.includes(doc.name)) {
			status = 'In Progress';
		}
		if (status == 'Pending') {
			status = 'Not Started';
		}
		return [__(status), colors[status], 'status,=,' + doc.status];
	},
	formatters: {
		import_type(value) {
			return {
				'Insert New Records': __('Insert'),
				'Update Existing Records': __('Update')
			}[value];
		}
	},
	hide_name_column: true
};



frappe.listview_settings['Journal Entry'] = {
	add_fields: ["voucher_type", "posting_date", "total_debit", "company", "user_remark"],
	get_indicator: function(doc) {
		if(doc.docstatus==0) {
			return [__("Draft", "red", "docstatus,=,0")]
		} else if(doc.docstatus==2) {
			return [__("Cancelled", "grey", "docstatus,=,2")]
		} else {
			return [__(doc.voucher_type), "blue", "voucher_type,=," + doc.voucher_type]
		}
	}
};
*/