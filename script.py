import requests

TOKEN = "test"
CHAT_ID = "test"

URL = "https://www.apple.com/fr/shop/refurbished/mac"

def send(msg):
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                  data={"chat_id": CHAT_ID, "text": msg})

def check():
    r = requests.get(URL)
TEST OK - ton bot fonctionne

check()
