import frappe
 
@frappe.whitelist()
def show_me():
    color = frappe.form_dict.get('color', 'black')
    return frappe.render_template("airplane_mode/www/show-me/index.html", {"color": color})
 