#!/usr/bin/env python3
"""
Cloud Migration Pipeline - Execution Script
This script runs the full migration process using the configuration in config.ini
"""

import os
import sys
import argparse
import logging
from datetime import datetime
from src.migration_pipeline import CloudMigrationPipeline

# Configure argument parser
parser = argparse.ArgumentParser(description='Run the cloud migration pipeline')
parser.add_argument('--config', default='config.ini', help='Path to configuration file')
parser.add_argument('--log-level', default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                    help='Logging level')
parser.add_argument('--validate-only', action='store_true', help='Run validation only, no data migration')
parser.add_argument('--tables', nargs='+', help='Specific tables to migrate (default: all in config)')
args = parser.parse_args()

# Configure logging
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
log_file = os.path.join(log_dir, f'migration_{timestamp}.log')

logging.basicConfig(
    level=getattr(logging, args.log_level),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('migration')

def main():
    """Run the migration pipeline with command line arguments"""
    try:
        logger.info(f"Starting migration with config file: {args.config}")
        
        # Initialize the pipeline
        pipeline = CloudMigrationPipeline(args.config)
        
        if args.tables:
            # Filter data sources to only include specified tables
            all_sources = pipeline.data_sources
            pipeline.data_sources = [s for s in all_sources if s['table'] in args.tables]
            logger.info(f"Filtered migration to tables: {', '.join(args.tables)}")
        
        if args.validate_only:
            # Only run validation
            logger.info("Running validation only mode")
            if not pipeline.connect_to_source_db():
                logger.error("Failed to connect to source database")
                return 1
                
            validation_results = []
            for source in pipeline.data_sources:
                table_name = source['table']
                logger.info(f"Validating table: {table_name}")
                result = pipeline.validate_migration(table_name)
                validation_results.append(result)
                
            success = all(r.get('validation_passed', False) for r in validation_results)
            
            if success:
                logger.info("All validations passed successfully!")
            else:
                failed = [r['table_name'] for r in validation_results if not r.get('validation_passed', False)]
                logger.error(f"Validation failed for tables: {', '.join(failed)}")
                return 1
        else:
            # Run full migration
            logger.info("Running full migration process")
            success = pipeline.run_migration()
            
            if not success:
                logger.error("Migration process failed")
                return 1
                
            logger.info("Migration completed successfully")
            
        return 0
        
    except Exception as e:
        logger.exception(f"Migration failed with error: {str(e)}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
