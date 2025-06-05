import requests

# Данные для доступа
BOT_TOKEN = '8036820330:AAEKTq6WvtSd2LqqKRM36P_WnLgxBJwxRCY'
CHAT_ID = '304521460'

# Текст сообщения
message = '✅ Тесты завершены. Ознакомьтесь с результатами.'

# Путь к отчёту Allure (если нужно прикрепить файл или ссылку)
# Можно заменить на путь к report.zip или URL Jenkins-отчёта
# Например: report_url = 'https://your-jenkins/job/your-job-name/allure'
report_url = None  # или строка URL

def send_telegram_message(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, data=payload)
    print(response.status_code)
    print(response.text)

if __name__ == '__main__':
    final_message = message
    if report_url:
        final_message += f"\n\n[Открыть отчёт]({report_url})"
    send_telegram_message(final_message)
