import frappe
from frappe import _ 

@frappe.whitelist()
def send_invitation_emails(meeting):
    meeting = frappe.get_doc("Meeting", meeting)
    meeting.check_permission("email")
    
    if meeting.status == "Planned":
        frappe.sendmail(
            recipients=[d.attendee for d in meeting.attendees],
            sender=frappe.session.user,
            subject=meeting.title,
            message=meeting.invitation_message,
            reference_doctype=meeting.doctype,
            reference_name=meeting.name
        )

        meeting.status = "Invitations sent"
        meeting.save()
        frappe.msgprint(_("Invitations sent successfully!"))
    else:
        frappe.msgprint(_("Meeting Status != Planned "))

@frappe.whitelist()
def get_meetings(start,end):
    if not frappe.has_permission('Meeting','read'):
        raise frappe.PermissionError
    
       
    
    filters =  {
                "start": start,
                "end": end
            }

    """ 
     Frappe.db.sql() && frappe.db.get_list() are the same,
     but Its recomended to use the get_list() method,
    """

    frappe.msgprint(frappe.db.sql("""
        select 
            name,
            timestamp('date',from_time) as start,
            timestamp('date', to_time) as end,
            title,status
        from tabMeeting
        where date between %(start)s and %(end)s """,{
            "start": start,
            "end": end
        },
       as_dict=0))

    frappe.msgprint(
        frappe.db.get_list('Meeting',
        fields=['name',
            'title','status'],
        as_list=True
     )
    )

    return frappe.db.sql("""
        select 
            name,
            timestamp('date',from_time) as start,
            timestamp('date', to_time) as end,
            title,status
        from tabMeeting
        where date between %(start)s and %(end)s """,
       {
            "start": start,
            "end": end
        },as_dict=0)