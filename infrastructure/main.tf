resource "azurerm_resource_group" "static_site" {
  name     = "rg-${var.service_name}"
  location = var.location
}

resource "azurerm_static_web_app" "static_site" {
  name                = var.service_name
  resource_group_name = azurerm_resource_group.static_site.name
  location            = azurerm_resource_group.static_site.location
  sku_tier            = "Free"
  sku_size            = "Free"
}
