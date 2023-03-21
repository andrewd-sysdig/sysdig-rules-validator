# sysdig-rules-validator

Use this to validate your `falco_local_rules.yaml` file before pushing to the Sysdig API

```bash
docker run -v $(pwd)/falco_rules_local.yaml:/falco_rules_local.yaml -e SECURE_API_TOKEN=xxxx -e API_ENDPOINT=https://app.au1.sysdig.com ghcr.io/andrewd-sysdig/sysdig-rules-validator:latest
```