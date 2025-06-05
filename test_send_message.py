import requests

BOT_TOKEN = "8036820330:AAEKTq6WvtSd2LqqKRM36P_WnLgxBJwxRCY"
CHAT_ID = "304521460"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": "🧪 Тестовая отправка сообщения из Python-скрипта",
}

response = requests.post(url, data=payload)
print(response.status_code)
print(response.text)
