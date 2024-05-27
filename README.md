End-to-End Data Engineering Project on AWS Cloud

This project demonstrates an end-to-end data engineering pipeline using AWS Cloud services. The pipeline includes a staging layer, an ETL process using AWS Glue, and a data warehouse. Once the data warehouse is populated, we use AWS Glue Crawler to create a database and table, and AWS Athena to query the data.

Project Overview
Staging Layer: Data is stored in an S3 bucket.
ETL Pipeline: AWS Glue is used to extract data from the staging layer, transform it, and load it into a data warehouse.
Data Warehouse: Data is stored in an S3 bucket in a structured format.
AWS Glue Crawler: Automatically creates a database and table schema based on the data in the data warehouse.
AWS Athena: Used to query the data stored in the data warehouse.
Architecture

Prerequisites
AWS Account
AWS CLI installed and configured
AWS IAM roles with necessary permissions for Glue, S3, and Athena
S3 bucket for staging and data warehouse
Setup
1. Staging Layer
Create an S3 bucket to store raw data.
Upload your data files to this bucket.
2. ETL Pipeline using AWS Glue
Create an AWS Glue Job:

Go to the AWS Glue console.
Create a new job.
Specify the IAM role with the necessary permissions.
Define the script to read data from the staging S3 bucket, transform it, and write it to another S3 bucket (data warehouse).
