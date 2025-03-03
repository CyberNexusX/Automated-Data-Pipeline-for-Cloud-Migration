# Azure Infrastructure Variables for Cloud Migration Pipeline

variable "resource_group_name" {
  description = "Name of the resource group to deploy resources into"
  type        = string
  default     = "rg-cloud-migration"
}

variable "location" {
  description = "Azure region to deploy resources in"
  type        = string
  default     = "East US"
}

variable "storage_account_name" {
  description = "Name of the storage account for migration data"
  type        = string
  default     = "samigrationdata"
}

variable "container_name" {
  description = "Name of the blob container for migration data"
  type        = string
  default     = "migration-data"
}

variable "data_factory_name" {
  description = "Name of the Data Factory instance"
  type        = string
  default     = "df-cloud-migration"
}

variable "environment" {
  description = "Deployment environment (dev, test, prod)"
  type        = string
  default     = "dev"
}

variable "tags" {
  description = "Tags to apply to all resources"
  type        = map(string)
  default = {
    Project     = "Cloud Migration"
    Environment = "Development"
    ManagedBy   = "Terraform"
  }
}

variable "azure_integration_runtime_compute_type" {
  description = "Compute type for the Azure Integration Runtime"
  type        = string
  default     = "General"
}

variable "azure_integration_runtime_core_count" {
  description = "Core count for the Azure Integration Runtime"
  type        = number
  default     = 8
}

variable "azure_integration_runtime_ttl" {
  description = "Time to live (in minutes) for the Azure Integration Runtime"
  type        = number
  default     = 60
}
