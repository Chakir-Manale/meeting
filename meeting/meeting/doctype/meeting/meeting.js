
frappe.ui.form.on('Meeting',  'validate',  function(frm) {
    if (frm.doc.date < frappe.datetime.get_today()) {
        msgprint('You cant select past date!');
        validated = false;
    } 
});

frappe.ui.form.on("Meeting Attendee",{
    attendee: function(frm,cdt,cdn){
        var attendee = frappe.model.get_doc(cdt,cdn);
        //if attendee selected, get full name
        if(attendee.attendee){
            frappe.call({
                method: "meeting.meeting.doctype.meeting.meeting.get_full_name",
                args: {
                    attendee: attendee.attendee
                },
                callback: function(r){
                    frappe.model.set_value(cdt,cdn,'full_name',r.message);
                }
            })
        }
        else{
            //if no attendee selected, free full name
            frappe.model.set_value(cdt,cdn,"full_name",null);
        }
    }
})

frappe.ui.form.on("Meeting",{
    send_invitations: function(frm){
        if(frm.doc.status === "Planned"){
            frappe.call({
                method: "meeting.api.send_invitation_emails",
                args: {
                    meeting: frm.doc.name
                }
            });
            
            setTimeout(function(){
                //location.reload();
                window.location.reload();
             }, 3000);
        }
    }
})