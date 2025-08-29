frappe.ready(function() {
  const urlParams = new URLSearchParams(window.location.search);
  const shop = urlParams.get("shop1");
  if (shop) {
    // Set hidden field 'shop'
    const shopField = document.querySelector('[data-fieldname="shop"] input');
    if (shopField) {
      shopField.value = shop;
    }
  }
});
