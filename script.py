import requests
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

print("TOKEN =", TOKEN)
print("CHAT_ID =", CHAT_ID)

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": "✅ TEST FINAL - ton bot fonctionne 🚀"
})

print("RESPONSE =", response.text)
``
