# IAM Configuration & Roles (GCP)

## Objectives
- Understand roles hierarchy
- Apply least privilege

## Checklist
- Replace primitive roles (Owner/Editor/Viewer) with predefined/custom roles
- Use IAM Conditions for scope-limited grants
- Regularly review IAM policy via Policy Analyzer

## Commands
gcloud projects get-iam-policy PROJECT_ID
gcloud iam roles create customRoleName --project=PROJECT_ID --file=role-definition.yaml

markdown
Copy code

## Learning points
- Audit IAM changes frequently
