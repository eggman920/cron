import requests

req = requests.session()

msg = 'cron test'

print(msg)

slack = ''
req.post(slack, json={"msg": msg})
