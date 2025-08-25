# Copyright (c) 2025, Tushar Prajapati  and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AirplaneFlight(Document):
	def on_submit(self):

		self.db_seat("status","complated")
	def autoname(self):
   		self.route = f"{self.source_airport.lower()}-to-{self.destination_airport.lower()}-{self.date_of_departure}"
