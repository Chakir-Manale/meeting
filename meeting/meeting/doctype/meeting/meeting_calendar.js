frappe.views.calendar["Meeting"] = {
    field_map:{
        "name":"name",
        "start": "start",
        "end": "end",
        "title": "title",
        "status": "status"
    },
    get_events_method:"meeting.api.get_meetings"
}