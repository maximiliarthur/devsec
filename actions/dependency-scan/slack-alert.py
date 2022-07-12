import json
from operator import itemgetter
import requests

def send_slack_message(payload, webhook):
    return requests.post(webhook, json.dumps(payload))

f = open('oast-results.json')
report_list = []
report_json = json.load(f)
items_detail=""
vuln_package = []
for item in report_json["affected_packages"]:
    vuln_package.append(item)
for package in vuln_package:
    print (report_json["affected_packages"][package]["name"])
    report_dict = {"name": report_json["affected_packages"][package]["name"], "version": report_json["affected_packages"][package]["version"]}
    report_list.append(report_dict)
print (report_list)
sorted_report_list = sorted(report_list, key=itemgetter('name'))
for item in sorted_report_list:
    items_detail += f"Name: `{item['name']}`\n" \
                    f"Version: `{item['version']}`\n"
print(items_detail)

webhook = "https://hooks.slack.com/services/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"
payload = {"text": items_detail, "username" : "dependencies-scanner"}
send_slack_message(payload, webhook)