import json
from operator import itemgetter
import requests

def send_slack_message(payload, webhook):
    return requests.post(webhook, json.dumps(payload))

f = open('output.json')
report_list = []
report_json = json.load(f)
items_detail=""

for item in report_json:
    report_dict = {"name": item['Description'], "file": item['File'], "lineNumber": item['StartLine']}
    report_list.append(report_dict)
sorted_report_list = sorted(report_list, key=itemgetter('file'))
for item in sorted_report_list:
    items_detail += f"Name: `{item['name']}`\n" \
                    f"File: `{item['file']}`\n" \
                    f"Line Number: `{item['lineNumber']}`\n"
print(items_detail)

webhook = "https://hooks.slack.com/services/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"
payload = {"text": items_detail, "username" : "secret-scanner"}
send_slack_message(payload, webhook)