output "default_host_name" {
  value       = azurerm_static_web_app.static_site.default_host_name
  description = "Default hostname for the static web app"
}

output "api_key" {
  value       = azurerm_static_web_app.static_site.api_key
  description = "API key for deploying content"
  sensitive   = true
}
