
frappe.ui.form.on('Meeting',  'validate',  function(frm) {
    if (frm.doc.date < frappe.datetime.get_today()) {
        msgprint('You cant select past date!');
        validated = false;
    } 
});