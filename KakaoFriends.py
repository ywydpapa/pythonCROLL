import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '4a41448985c7ee13308b5233ea60f811'
redirect_uri = 'https://example.com/oauth'
authorize_code = '1y-nLc6erC96k8S0khLZem9SiZigmGZo0BNNLVk9Cj10EQAAAYNE7k_O'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
with open(r"C:\Users\DELL\Documents\kakao_code.json","w") as fp:
    json.dump(tokens, fp)