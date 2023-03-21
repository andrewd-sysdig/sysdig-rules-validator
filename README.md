# Sysdig Rules Validator 

Use this to validate your `falco_local_rules.yaml` file before pushing to the Sysdig API. Useful for testing your file in pipeline.

Straight forward - just run the below docker run command in the same directory as your falco_rules_local.yaml (Custom rules file)

```bash
docker run -v $(pwd)/falco_rules_local.yaml:/home/app/falco_rules_local.yaml -e SECURE_API_TOKEN=xxxx -e API_ENDPOINT=https://app.au1.sysdig.com ghcr.io/andrewd-sysdig/sysdig-rules-validator:latestsysdig-rules-validator:latest
Tue Mar 21 10:10:24 2023: Falco version: 0.34.1 (x86_64)
Tue Mar 21 10:10:24 2023: Falco initialized with configuration file: /falco/etc/falco/falco.yaml
Tue Mar 21 10:10:24 2023: Validating rules file(s):
Tue Mar 21 10:10:24 2023:    threat_intelligence_feed.yaml
Tue Mar 21 10:10:24 2023:    aws_cloudtrail.yaml
Tue Mar 21 10:10:24 2023:    azure_platformlogs.yaml
Tue Mar 21 10:10:24 2023:    cloud.yaml
Tue Mar 21 10:10:24 2023:    falco_rules.yaml
Tue Mar 21 10:10:24 2023:    gcp_auditlog.yaml
Tue Mar 21 10:10:24 2023:    k8s_audit_rules.yaml
Tue Mar 21 10:10:24 2023:    falco_rules_local.yaml
Newest Default Sysdig rules downloaded
(b'threat_intelligence_feed.yaml: Ok, with warnings\naws_cloudtrail.yaml: Ok, with warnings\nazure_platformlogs.yaml: Ok, with warnings\ncloud.yaml: Ok, with warnings\nfalco_rules.yaml: Ok, with warnings\ngcp_auditlog.yaml: Ok, with warnings\nk8s_audit_rules.yaml: Ok, with warnings\nfalco_rules_local.yaml: Ok, with warnings\n', None)
```