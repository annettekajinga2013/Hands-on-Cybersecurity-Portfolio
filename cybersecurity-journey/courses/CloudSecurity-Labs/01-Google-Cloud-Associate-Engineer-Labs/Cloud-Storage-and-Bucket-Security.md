# Cloud-Storage-and-Bucket-Security
# Cloud Storage & Bucket Security (GCP)

## Objectives
- Secure buckets (uniform access)
- Prevent public exposure
- Enable logging & retention

## Prereqs
- gcloud configured
- project owner or storage admin

## Tasks (commands)
1. Create bucket (uniform access)

gsutil mb -p PROJECT_ID -c STANDARD -l REGION gs://my-secure-bucket/
gsutil uniformbucketlevelaccess set on gs://my-secure-bucket

2. Block public access
gsutil iam ch allUsers:objectViewer gs://my-secure-bucket # (only to test then remove)
gsutil iam ch -d allUsers:objectViewer gs://my-secure-bucket

markdown
Copy code

3. Enable logging
gsutil logging set on -b gs://log-bucket -o access gs://my-secure-bucket

pgsql
Copy code

4. Enable object versioning
gsutil versioning set on gs://my-secure-bucket

markdown
Copy code

## Tests
- Attempt public GET (should fail)
- Check audit logs in Cloud Logging

## Learning points
- Uniform bucket-level access simplifies IAM model
- Versioning + retention help recover from accidental deletes
