# Serverless ETL Pipeline using AWS

## Project Overview

This project demonstrates a serverless ETL (Extract, Transform, Load) pipeline using AWS services. The application fetches live weather data from the OpenWeather API, stores the raw JSON in Amazon S3, transforms the data, and saves the processed records in Amazon DynamoDB. AWS Lambda performs the ETL process, while Amazon CloudWatch records execution logs.

## AWS Services Used

- AWS Lambda
- Amazon S3
- Amazon DynamoDB
- Amazon CloudWatch
- AWS CodeBuild
- AWS CodePipeline

## Other Technologies

- Python 3.11+
- GitHub
- GitHub Actions
- OpenWeather API

## Project Workflow

```text
OpenWeather API
        │
        ▼
AWS Lambda
        │
        ▼
Amazon S3 (Raw JSON)
        │
        ▼
Data Transformation
        │
        ▼
Amazon DynamoDB
        │
        ▼
CloudWatch Logs
```

## Features

- Fetches live weather data using OpenWeather API
- Stores raw JSON data in Amazon S3
- Transforms weather data
- Stores processed records in DynamoDB
- Generates CloudWatch logs
- CI/CD ready using GitHub Actions and AWS CodePipeline

## Project Structure

```text
serverless-etl-pipeline/
│── lambda_function.py
│── requirements.txt
│── buildspec.yml
│── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

## Author

**Hareesh Singh**

GitHub: https://github.com/coderhjs2523