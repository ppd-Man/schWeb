import requests

url = "http://34.81.78.27/PayPayDrinkBackend/api/auth/login"

payload = "{\r\n    \"account\":\"api\",\r\n    \"password\":\".iaKVMVf_8h_1i9y\"\r\n}"
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)