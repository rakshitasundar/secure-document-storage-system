# Secure Document Storage System

## Project Overview

The Secure Document Storage System was developed as part of my Cloud Computing Internship at Edutantr using Amazon Web Services (AWS).

The project provides a secure cloud-based environment for storing and managing documents with controlled access and monitoring.

## Objectives

- Store documents securely using Amazon S3.
- Control access using AWS IAM.
- Protect stored documents using SSE-S3 encryption.
- Use AWS Lambda for serverless processing.
- Monitor Lambda execution using Amazon CloudWatch.
- Test and verify the configured AWS resources.

## AWS Services Used

### Amazon S3
Used as the cloud storage service for storing documents.

### AWS IAM
Used to configure access permissions and the Lambda execution role.

### AWS Lambda
Used for serverless processing and retrieving the documents stored in S3.

### Amazon CloudWatch
Used to monitor Lambda execution and view logs.

### SSE-S3
Used to provide server-side encryption for stored objects.

## System Workflow

User → AWS IAM → Amazon S3 → AWS Lambda → CloudWatch

1. Documents are stored in the Amazon S3 bucket.
2. IAM controls the required access permissions.
3. SSE-S3 protects the stored objects.
4. AWS Lambda processes the required S3 operations.
5. CloudWatch is used to monitor Lambda execution.

## Implementation

The project was implemented using Python and the AWS SDK for Python (Boto3).

The Lambda function connects to the S3 bucket and retrieves the available objects, including their file names and sizes.

## Testing

The Lambda function was tested through the AWS Lambda console to verify successful execution and access to the configured S3 bucket.

## Technologies

- Python
- Boto3
- Amazon S3
- AWS IAM
- AWS Lambda
- Amazon CloudWatch
- SSE-S3 Encryption

## Internship

**Domain:** Cloud Computing  
**Organization:** Edutantr

## Author

**Rakshita S K S**
