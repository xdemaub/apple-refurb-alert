import requests
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

print("DEBUG TOKEN:", TOKEN)
print("DEBUG CHAT_ID:", CHAT_ID)

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r = requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })
    print("Telegram response:", r.text)

# ✅ TEST FORCÉ
send("✅ TEST OK - si tu vois ce message, tout fonctionne !")
