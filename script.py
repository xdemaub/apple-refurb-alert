import requests
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": " BOT OK (test final)"
    }
)

print("message envoyé")
