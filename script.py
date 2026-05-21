import requests
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

print("TOKEN =", TOKEN)
print("CHAT_ID =", CHAT_ID)

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

try:
    response = requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": "✅ TEST FINAL - BOT OK 🚀"
    })

    print("STATUS CODE =", response.status_code)
    print("RESPONSE =", response.text)

except Exception as e:
    print("ERROR =", e)
