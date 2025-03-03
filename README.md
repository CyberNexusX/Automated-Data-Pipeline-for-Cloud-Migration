# Automated Data Pipeline for Cloud Migration

A scalable ETL pipeline for seamless migration of large datasets from on-premises systems to Azure cloud storage, optimizing for both performance and cost efficiency.

![Pipeline Architecture](https://via.placeholder.com/800x400?text=Cloud+Migration+Pipeline+Architecture)

## Features

- **Automated ETL Process**: Extract data from on-premises SQL databases and load into Azure Blob Storage with minimal manual intervention
- **Performance Optimized**: Process large datasets with configurable batching and parallel execution
- **Cost Efficient**: Dynamic resource allocation and scheduled operations to minimize cloud costs
- **Data Validation**: Built-in validation to ensure data integrity throughout the migration
- **Infrastructure as Code**: Complete Terraform configuration for Azure resource provisioning
- **Monitoring & Logging**: Comprehensive logging and pipeline run monitoring

## Technologies

- Azure Data Factory
- Python 3.8+
- SQL Server
- Azure Blob Storage
- Terraform
- Pandas

## Getting Started

### Prerequisites

- Azure Subscription
- Python 3.8 or higher
- Terraform CLI
- Azure CLI
- Access to on-premises SQL Server

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cloud-migration-pipeline.git
   cd cloud-migration-pipeline
   ```

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the migration settings:
   ```bash
   cp config.ini.example config.ini
   # Edit config.ini with your Azure and database details
   ```

4. Deploy the infrastructure:
   ```bash
   cd terraform
   terraform init
   terraform apply
   ```

### Usage

1. Prepare your migration configuration:
   ```
   # Edit the DataSources section in config.ini to specify which tables to migrate
   ```

2. Run the migration:
   ```bash
   python run_migration.py
   ```

3. Validate the results:
   ```bash
   python validate_migration.py
   ```

## Project Structure

```
cloud-migration-pipeline/
├── src/
│   ├── __init__.py
│   ├── migration_pipeline.py     # Main pipeline implementation
│   ├── validators.py             # Data validation utilities
│   └── utils.py                  # Helper functions
├── terraform/
│   ├── main.tf                   # Main Terraform configuration
│   ├── variables.tf              # Input variables
│   └── outputs.tf                # Output values
├── docs/
│   ├── architecture.md           # Detailed architecture documentation
│   ├── performance_tuning.md     # Performance optimization guide
│   └── troubleshooting.md        # Common issues and solutions
├── config.ini.example            # Example configuration
├── requirements.txt              # Python dependencies
├── run_migration.py              # Migration execution script
└── README.md                     # Project documentation
```

## Configuration

The `config.ini` file contains all necessary configurations:

```ini
[Azure]
SubscriptionId = your-subscription-id
ResourceGroup = your-resource-group
DataFactoryName = your-data-factory
StorageAccountName = your-storage-account
StorageAccountKey = your-storage-account-key
ContainerName = migration-data

[OnPremDB]
Server = your-server-name
Database = your-database-name
Username = your-username
Password = your-password

[Migration]
BatchSize = 10000
ParallelThreads = 4
DataSources = [{"table": "Customers", "query": "SELECT * FROM Customers"}, {"table": "Orders"}, {"table": "Products"}]
```

## Performance Tuning

For large datasets:
- Increase `BatchSize` for tables with simple schemas
- Increase `ParallelThreads` on systems with more resources
- Use custom SQL queries to filter data when full table migration isn't needed

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Azure Data Factory documentation
- Python Azure SDK team
- Terraform Azure Provider documentation
