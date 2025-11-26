# CloudTrail & GuardDuty (AWS)

## Objectives
- Enable organization-wide CloudTrail
- Enable GuardDuty and analyze sample findings

## Tasks
1. Create multi-region CloudTrail and send logs to S3 + CloudWatch Logs
2. Enable GuardDuty for the account (or org)
3. Simulate suspicious behavior (e.g., console login from new IP) and observe findings

## Notes
- Centralize trails and bucket locking to prevent tampering
- Connect GuardDuty to AWS Security Hub for consolidated view

