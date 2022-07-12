import json
from operator import itemgetter
import requests
import sys

def send_slack_message(payload, webhook):
    return requests.post(webhook, json.dumps(payload))

f = open('output.json')
report_list = []
report_json = json.load(f)
items_detail="=== SECRET SCAN ===\n"

for item in report_json:
    report_dict = {"name": item['Description'], "file": item['File'], "lineNumber": item['StartLine']}
    report_list.append(report_dict)
sorted_report_list = sorted(report_list, key=itemgetter('file'))
for item in sorted_report_list:
    items_detail += f"Name: `{item['name']}`\n" \
                    f"File: `{item['file']}`\n" \
                    f"Line Number: `{item['lineNumber']}`\n"
print(items_detail)

webhook = sys.argv[1]
payload = {"text": items_detail}
send_slack_message(payload, webhook)