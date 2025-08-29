import frappe
from frappe import _

#@frappe.whitelist(allow_guest=False)  # Only logged-in users can call
#def get_shops():
#   shops = frappe.get_all(
#       "Shop1",
#        fields=[ "shop_name", "shop_type", "shop_number"]
#   )
#    return shops


#def post_shops():
#    shops = frappe.post_all(
#        "Shop Type",
#        fields=["shop_name", "shop_type", "enabled"]
#    )
#    return shops

#import frappe

# import frappe

# @frappe.whitelist(allow_guest=True)
# def post_shops(shop_name, shop_details=None):
#     doc = frappe.get_doc({
#         "doctype": "Shop1",
#         "shop_name": shop_name,
#         "shop_details": shop_details
#     })
#     # bypass Guest permission check
#     doc.insert(ignore_permissions=True)
#     frappe.db.commit()
#     return doc


# @frappe.whitelist(allow_guest=True)
# def post_shops(shop_name, shop_number=None, shop_type=None):
#     doc = frappe.get_doc({
#         "doctype": "Shop1",
#         "shop_name": shop_name,
#         "shop_number": shop_number,
#         "shop_type": shop_type,
#         "name": f"SHOP-{shop_number or frappe.utils.now_datetime().strftime('%Y%m%d%H%M%S')}"
#     })
#     doc.insert(ignore_permissions=True)
#     frappe.db.commit()
#     return doc



@frappe.whitelist(allow_guest=True)
def post_shops(shop_name, shop_number, shop_type):
    # Create Shop1 document
    doc = frappe.get_doc({
        "doctype": "Shop1",
        "shop_name": shop_name,
        "shop_number": shop_number,
        "shop_type": shop_type,
        # Generate unique name from shop_number
        "name": f"SHOP-{shop_number}"
    })
    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    # Return the inserted document as response
    return {
        "status": "success",
        "message": "Shop created successfully",
        "data": {
            "name": doc.name,
            "shop_name": doc.shop_name,
            "shop_number": doc.shop_number,
            "shop_type": doc.shop_type
        }
    }
