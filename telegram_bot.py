import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
USE_TEST_MODE = not (BOT_TOKEN and CHAT_ID)

if USE_TEST_MODE:
    print("⚠️  TEST MODE: Using console alerts instead of Telegram")

def send_alert(address, private, balance):
    msg = f"💰 Found!\nAddress: {address}\nBalance: {balance}\nKey: {private}"
    
    if USE_TEST_MODE:
        print("\n" + "="*60)
        print("🚨 ALERT - BALANCE FOUND!")
        print("="*60)
        print(msg)
        print("="*60 + "\n")
    else:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
