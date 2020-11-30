frappe.listview_settings['Meeting'] = {
	
	get_indicator: function(doc) {
        return [__(doc.status),{
			"Planned": "blue",
			"Invitations sent": "orange",
			"In Progress": "red",
			"Completed": "green",
			"Cancelled": "darkgrey"
		}[doc.status], "status,=," + doc.status];
    }
    
};

/*
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