import frappe
from frappe.model.document import Document
 
class RentPayment(Document):
 
 
 def send_rent_reminders():
    settings = frappe.get_single("Airport Shop Settings")
    if not settings.enable_rent_reminders:
        return
 
    contracts = frappe.get_all("Contract",
        fields=["name", "tenant", "rent_amount", "end_date"],
    )
    for contract in contracts:
        tenant = frappe.get_doc("Tenant", contract.tenant)
        frappe.sendmail(
            recipients=tenant.email,
            subject="Rent Reminder",
            message=f"Dear {tenant.tenant_name},<br>Your rent of {contract.rent_amount} is due this month.<br>Regards,<br>Airport Authority"
        )