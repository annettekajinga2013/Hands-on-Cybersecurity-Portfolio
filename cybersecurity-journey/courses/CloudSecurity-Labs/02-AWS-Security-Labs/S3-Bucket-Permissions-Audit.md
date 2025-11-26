# S3 Bucket Permissions Audit

## Objectives
- Find public buckets and misconfigurations
- Apply Block Public Access and correct ACLs

## Commands
aws s3api list-buckets
aws s3api get-bucket-acl --bucket BUCKET_NAME

markdown
Copy code

## Learning points
- MFA Delete adds an additional safeguard for destructive operations
