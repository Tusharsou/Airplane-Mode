# Copyright (c) 2025, Tushar Prajapati  and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.background_jobs import enqueue


class AirplaneFlight(Document):
	def on_submit(self):

		self.db_seat("status","complated")
	def autoname(self):
   		self.route = f"{self.source_airport.lower()}-to-{self.destination_airport.lower()}-{self.date_of_departure}"
               

def on_update(doc, method):
    # Check if gate changed
		if doc.has_value_changed("gate_number"):
        		enqueue(update_tickets_gate, flight=doc.name, new_gate=doc.gate_number)

def update_tickets_gate(flight, new_gate):
    tickets = frappe.get_all("Airplane Ticket", filters={"airplane_flight": flight}, pluck="name")
    for ticket in tickets:
        frappe.db.set_value("Airplane Ticket", ticket, "gate_number", new_gate)
    frappe.db.commit()
