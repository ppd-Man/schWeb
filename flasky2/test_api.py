import requests
import payconfiguration
import json
from datetime import datetime

def get_api_token():
    url = "http://34.81.78.27/PayPayDrinkBackend/api/auth/login"

    payload = "{\r\n    \"account\":\"api\",\r\n    \"password\":\".iaKVMVf_8h_1i9y\"\r\n}"
    headers = { 'Content-Type': 'application/json' }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    responseJson = json.loads(response.text)
    payconfiguration.API_TOKEN = responseJson['access_token']  
    
def checkToken():

    url = f"http://34.81.78.27/PayPayDrinkBackend/api/auth/me?token={payconfiguration.API_TOKEN}"

    payload={}
    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.status_code)
    print(response.text)
    return response.status_code
def report_cup_num(pay_ip,cup_num):
    url = "http://34.81.78.27/PayPayDrinkBackend/api/reportCup?token={payconfiguration.API_TOKEN}"
    today=datetime.now()
    todayStr=today.strftime('%Y-%m-%d %H:%M:%S')
    # payload = "{\r\n    \"ip\":\"192.168.1.1\", /* 樹苺派IP */\r\n    \"date\":\"2021-07-21 01:22:22\", /* 做完的日期時間 */\r\n    \"cupnum\":\"A002\" /* 當初傳過去的cupnum */\r\n}"
    payload = f"{ 'ip':'{ip}','date':'{todayStr}','cpunum':'{cup_num}'}"
    headers = { 'Content-Type': 'application/json' }
   
    
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    
    
def main():    
    get_api_token()
    checkToken()
    # report_cup_num("1.2.3.4",'A1234')
    
    

main()