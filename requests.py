import requests

url = "https://voting-vote-producer.r7.com/vote"
body = {'voting_id': '302', "alternative_id": "760"}
x = requests.post(url, data = body)
print(x.text)
