import json
from operator import itemgetter
import requests
import sys

def send_slack_message(payload, webhook):
    return requests.post(webhook, json.dumps(payload))

f = open('bandit-output.json')
report_list = []
report_json = json.load(f)
items_detail="=== Static Scan ===\n"
vuln = []
for item in report_json["results"]:
    vuln.append(item)
for v in vuln:
    print (v["code"])
    report_dict = {"code": v["code"], "severity": v["issue_severity"], "lineNumber": v["line_number"], "fileName":v["filename"]}
    report_list.append(report_dict)
sorted_report_list = sorted(report_list, key=itemgetter('severity'))
for item in sorted_report_list:
    items_detail += f"Code: `{item['code']}`\n" \
                    f"Severity: `{item['severity']}`\n" \
                    f"File Name: `{item['fileName']}`\n" \
                    f"Line Number: `{item['lineNumber']}`\n"
print(items_detail)

webhook = sys.argv[1]
payload = {"text": items_detail}
send_slack_message(payload, webhook)