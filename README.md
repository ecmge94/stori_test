# Thumbnail Generator

## Introduction

Welcome to the Thumbnail Generator project! Below, you'll find all the necessary code and instructions to get started.

## Recommendations

1. **Upload Code to AWS Bucket:** Before deploying the code to AWS Lambda, make sure to upload it to an AWS S3 bucket. Use the repository clone for this purpose. It's important to note that we're working with Lambda, so you may need to make adjustments, such as removing unnecessary folders to ensure AWS can read the code correctly.

2. **Code Editing:** Due to the size of the project and dependencies like the PIL library, it's not feasible to edit the code directly within the Lambda console.

3. **Deployment with CloudFormation:** Execute the `stori_test.yaml` file in the CloudFormation service to create the necessary resources in AWS, including two S3 buckets and the Lambda function.

4. **Lambda Testing:** Before deploying the Lambda function in real-time, it's advisable to thoroughly test it.

## Architecture

In this project, all methods are included in a single file. While this approach offers the advantage of high cohesion by consolidating all parts of the code in one place, it may result in slightly longer execution times.
