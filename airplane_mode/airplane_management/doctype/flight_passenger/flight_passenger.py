# Copyright (c) 2025, Tushar Prajapati  and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	def before_save(self):

		first_name = self.first_name or ""
		last_name = self.last_name or ""

		self.full_name = f"{first_name} {last_name}".strip()

	
