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