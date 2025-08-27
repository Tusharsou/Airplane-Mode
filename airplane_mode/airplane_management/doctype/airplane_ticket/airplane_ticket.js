frappe.ui.form.on("Airplane Ticket", {
    refresh: function(frm) {
        // Add the custom button
        frm.add_custom_button("Assign Seat", function() {
            // Show dialog with input field
            let d = new frappe.ui.Dialog({
                title: "Assign Seat",
                fields: [
                    {
                        label: "Seat Number",
                        fieldname: "seat_number",
                        fieldtype: "Data",
                        reqd: 1
                    }
                ],
                primary_action_label: "Set Seat",
                primary_action(values) {
                    // Set the seat field in the form
                    frm.set_value("seat", values.seat_number);
                    d.hide();
                }
            });

            d.show();
        });
    }
});
