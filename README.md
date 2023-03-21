# Sysdig Rules Validator 

Use this to validate your `falco_local_rules.yaml` file before pushing to the Sysdig API. Useful for testing your file in pipeline.

```bash
docker run -v $(pwd)/falco_rules_local.yaml:/home/app/falco_rules_local.yaml -e SECURE_API_TOKEN=xxxx -e API_ENDPOINT=https://app.au1.sysdig.com ghcr.io/andrewd-sysdig/sysdig-rules-validator:latest
```