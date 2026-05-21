import requests
import os

URL = "https://www.apple.com/fr/shop/refurbished/mac"

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def check():
    response = requests.get(URL)
    
    if "MacBook Air 13 pouces reconditionné avec puce Apple M5" in response.text:
        send(" MacBook M5 détecté sur Apple Refurb !\n https://www.apple.com/fr/shop/refurbished/mac")
        print("M5 trouvé")
    else:
        print("Rien trouvé")

check()
