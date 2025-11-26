# Compute Engine Instance Security (GCP)

## Objectives
- Harden VM, restrict SSH
- Use IAM & service accounts safely

## Tasks
- Use images with security patches (Debian/Ubuntu LTS)
- Disable external IPs for backend VMs:
  - Create VM without external IP in subnet
- Use Cloud IAP for SSH:
  - Enable OS Login and IAP tunneling
- Configure firewall rules (allow only necessary ports)
- Limit service account scopes and use custom roles

## Quick commands
gcloud compute instances create my-vm --no-address --zone=ZONE --machine-type=e2-medium
gcloud compute ssh --tunnel-through-iap my-vm --zone=ZONE

markdown
Copy code

## Learning points
- External IPs increase remote attack surface
- OS Login + IAP centralizes access control and logs
