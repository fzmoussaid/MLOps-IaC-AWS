# Build necessary infrastructure for deploying an ML model

## Source code:

`main.tf` deploys necessary infrastructure resources for deploying the ML model:

- AWS Sagemaker Model
- AWS Sagemaker Endpoint Configuration
- AWS Sagemaker Serverless endpoint
- AWS Lambda for inference

## Building the infrastructure

Install terraform on your local machine refering [this page](https://developer.hashicorp.com/terraform/install)

Create IAM user with necessary permissions, generate access key for the user, set up terraform configuration to use these credentials.

Create `terraform.tfvars` file to store the following variables:

```
access_key = "your-aws-access-key"
secret_key = "your-secret-key"
account_id = "you-account-id"
```

Run `terraform init` to initiate terraform project.

Run `terraform plan` to plan infrastructure building. This command will show you the resources that will be created/updated/deleted in GCP.

Run `terraform apply` to actually build the infrastructure defined in terraform configuration files.
