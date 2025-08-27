# Copyright (c) 2025, Tushar Prajapati  and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document


class AirplaneTicket(Document):
	def before_save(self):

		total = self.flight_price or 0

		if self.get("add_ons"):
			for addon in self .add_ons:
				total += addon.amount or 0

		self.total_amount = total


	def before_insert(self):

		if not self.seat:
			self.seat = self.get_next_available_seat()

		if not self.route:
			self.route = f"{self.airplane.lower()}-{self.source_airport_code.lower()}-to-{self.destination_airport_code.lower()}-{frappe.generate_hash(length=6)}"


	def get_next_available_seat(self):

		seat_letters = ["A", "B", "C", "D", "E"]

		while True:
			seat_number = random.randint(1,99)
			seat_letter = random.choice(seat_letters)
			seat = f"{seat_number}{seat_letter}"

			exists = frappe.db.exists(
				"Airplane Ticket",
				{"flight": self.flight,"seat": seat}
			)

			if not exists:
				return seat  

class AirplaneTicket(Document):
    def validate(self):
        self.check_capacity_limit()

    def check_capacity_limit(self):
        if not self.airplane_flight:
            return

        # Get the linked airplane flight
        flight = frappe.get_doc("Airplane Flight", self.airplane_flight)

        if not flight.airplane:
            return

        # Get airplane capacity
        capacity = frappe.db.get_value("Airplane", flight.airplane, "capacity")

        # Count existing tickets for this flight (exclude current one if updating)
        booked_tickets = frappe.db.count(
            "Airplane Ticket",
            filters={
                "airplane_flight": self.airplane_flight,
                "name": ["!=", self.name]   # exclude current ticket in update
            }
        )

        if booked_tickets >= capacity:
            frappe.throw(
                f"Cannot create ticket. Airplane is full! "
                f"({booked_tickets}/{capacity} seats already booked)"
            )
       	

