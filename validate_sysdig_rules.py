import requests
import os
import subprocess

if os.getenv('SECURE_API_TOKEN') is not None:
    SECURE_API_TOKEN = os.getenv('SECURE_API_TOKEN')
else:
    print("Error: SECURE_API_TOKEN not set")
    exit(1)

if os.getenv('API_ENDPOINT') is not None:
    API_ENDPOINT = os.getenv('API_ENDPOINT')
else:
    print("Error: API_ENDPOINT not set")
    exit(1)

API_HEADERS = {
  'Authorization': 'Bearer ' + SECURE_API_TOKEN,
  'Content-Type': 'application/json'
}

# Need to download the latest default rules as these are needed since the local rules may rely or clash with them
url = API_ENDPOINT + '/api/settings/falco/newestDefaultRulesFiles'
r = requests.request("GET", url, headers=API_HEADERS)

if r.status_code == 200:
    files = (r.json()['newestDefaultFalcoRulesFiles']['files'])
    for file in files:
        f = open(file['name'], "w")
        f.write(file['content'])
    print("Newest Default Sysdig rules downloaded", flush=True)
        
elif r.status_code != 200:
    print("The Sysdig API did not return a HTTP 200 (OK) response. Response Code: {0}, Response Text: {1}".format(r.status_code, r.response_text))

# Execute falco -V to validate the falco rules
print("Running Falco Rule validation...", flush=True)
cmd_str="/falco/usr/bin/falco -c /falco/etc/falco/falco.yaml -V threat_intelligence_feed.yaml -V aws_cloudtrail.yaml -V azure_platformlogs.yaml -V cloud.yaml -V falco_rules.yaml -V gcp_auditlog.yaml -V k8s_audit_rules.yaml -V falco_rules_local.yaml"
p = subprocess.Popen(cmd_str, shell=True, stdout=subprocess.PIPE)
stdout = p.communicate()
print(stdout[0].decode('utf-8'))

exit(p.returncode)