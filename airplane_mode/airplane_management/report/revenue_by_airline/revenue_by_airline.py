import frappe
from frappe.utils import flt
 
def execute(filters=None):
    # Get all airlines
    airlines = frappe.get_all("Airline", fields=["name"])
 
    # Create a dict for default 0 revenue
    revenue_map = {airline.name: 0 for airline in airlines}
 
    # Fetch revenue data
    data = frappe.db.get_all(
        "Airline Revenue",
        fields=["airline", "revenue"],
        group_by="airline"
    )
 
    # Aggregate revenue
    for row in data:
        revenue_map[row["airline"]] = flt(row["revenue"])
 
    # Prepare final data for the table
    result = []
    total_revenue = 0
 
    for airline in airlines:
        rev = revenue_map.get(airline.name, 0)
        result.append([airline.name, rev])
        total_revenue += rev
 
    # Columns
    columns = [
        {
            "label": "Airline",
            "fieldname": "airline",
            "fieldtype": "Link",
            "options": "Airline",
            "width": 200
        },
        {
            "label": "Revenue",
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "width": 150
        }
    ]
 
    # Chart
    chart = {
        "data": {
            "labels": list(revenue_map.keys()),
            "datasets": [
                {
                    "name": "Revenue",
                    "values": list(revenue_map.values())
                }
            ]
        },
        "type": "donut"
    }
 
    # Summary Section
    summary = [
        {
            "label": "Total Revenue",
            "value": total_revenue,
            "indicator": "Green"
        }
    ]
 
    # Total Row
    total_row = ["Total", total_revenue]
 
    return columns, result, None, chart, summary, total_row
 
 