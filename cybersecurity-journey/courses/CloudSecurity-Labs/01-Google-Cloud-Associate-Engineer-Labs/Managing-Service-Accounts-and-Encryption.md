# Service Accounts & Encryption (GCP)

## Objectives
- Control service account keys
- Use KMS for CMKs

## Tasks
- Create dedicated service accounts per workload
- Avoid long-lived SA keys
- Use Workload Identity or short-lived tokens for GKE
- Encrypt with Cloud KMS and rotate keys

## Commands
gcloud iam service-accounts create sa-name --display-name="service account for app"
gcloud kms keys create key-name --location global --keyring my-ring --purpose encryption

markdown
Copy code

## Learning points
- Over-permissioned SAs are high risk
