# Sysdig Rules Validator 

This container can be used to validate your `falco_local_rules.yaml` file before pushing to the Sysdig API, which maybe useful to use in your pipeline.

## Usage

Run the following docker command in the same directory as your `falco_rules_local.yaml` (Custom rules file)

```bash
docker run -v $(pwd)/falco_rules_local.yaml:/home/app/falco_rules_local.yaml -e SECURE_API_TOKEN=xxxx -e API_ENDPOINT=https://app.au1.sysdig.com ghcr.io/andrewd-sysdig/sysdig-rules-validator:latestsysdig-rules-validator:latest
Newest Default Sysdig rules downloaded
Running Falco Rule validation...
Tue Mar 21 11:49:45 2023: Falco version: 0.34.1 (x86_64)
Tue Mar 21 11:49:45 2023: Falco initialized with configuration file: /falco/etc/falco/falco.yaml
Tue Mar 21 11:49:45 2023: Validating rules file(s):
Tue Mar 21 11:49:45 2023:    threat_intelligence_feed.yaml
Tue Mar 21 11:49:45 2023:    aws_cloudtrail.yaml
Tue Mar 21 11:49:45 2023:    azure_platformlogs.yaml
Tue Mar 21 11:49:45 2023:    cloud.yaml
Tue Mar 21 11:49:45 2023:    falco_rules.yaml
Tue Mar 21 11:49:45 2023:    gcp_auditlog.yaml
Tue Mar 21 11:49:45 2023:    k8s_audit_rules.yaml
Tue Mar 21 11:49:45 2023:    falco_rules_local.yaml
threat_intelligence_feed.yaml: Ok, with warnings
aws_cloudtrail.yaml: Ok, with warnings
azure_platformlogs.yaml: Ok, with warnings
cloud.yaml: Ok, with warnings
falco_rules.yaml: Ok, with warnings
gcp_auditlog.yaml: Ok, with warnings
k8s_audit_rules.yaml: Ok, with warnings
falco_rules_local.yaml: Ok, with warnings
```