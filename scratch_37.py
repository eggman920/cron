import requests

req = requests.session()

msg = 'cron test'

print(msg)

slack = 'https://hooks.slack.com/workflows/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'
req.post(slack, json={"msg": msg})
