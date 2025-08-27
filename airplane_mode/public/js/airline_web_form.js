frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        frm.add_custom_button(__('Official Website'), function() {
            if (frm.doc.website) {
                window.open(frm.doc.website, '_blank');
            } else {
                frappe.msgprint(__('No website found for this airline.'));
            }
        });
    }
});