import requests
import json
from bs4 import BeautifulSoup
import time


def get_price(com_code):
    url = 'https://finance.naver.com/item/main.nhn?code=' + com_code
    response = requests.get(url, headers={'User-agent':'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    no_today = soup.find('p',{'class':'no_today'})
    blind_now = no_today.find('span',{'class':'blind'})
    return blind_now.text


def sendKakaoMessage(text):
    header = {"Authorization": 'Bearer ' + KAKAO_TOKEN}

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    post = {
        "object_type": "text",
        "text": text,
        "link" : {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title":"바로확인"

    }

    data = {"template_object" : json.dumps(post)}

    return requests.post(url, headers=header, data=data)

KAKAO_TOKEN = "xanAZ2qGcEBxdEH80zTlJSQ2aK2-bO7DNrxyLQbrCilvuQAAAYND2nGw"

try:
    while True:
        text = "삼성전자 현재가격은 " + get_price("005930")+"원 입니다."
        print(sendKakaoMessage(text).text)
        time.sleep(60)

except KeyboardInterrupt:
    pass
