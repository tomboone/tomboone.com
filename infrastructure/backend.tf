terraform {
  backend "azurerm" {
    resource_group_name  = "rg-tbc-app-services"
    storage_account_name = "tbcterraformstate"
    container_name       = "tfstate"
    key                  = "tomboone-dot-com.tfstate"
    use_oidc             = true
  }
}
