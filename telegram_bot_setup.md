# 🤖 Telegram Bot Setup - @fadal_awareness_bot

## ✅ Bot Token (ADDED)
Token-ka waa lagu daray `.env` file-ka.

## 📝 Bot Description (U Dir BotFather)

Waxaad BotFather-ka u diri kartaa description-kan:

```
🔍 Bitcoin Scanner Alert Bot

I send real-time notifications when Bitcoin wallets with balance are discovered during testnet research scans.

⚠️ EDUCATIONAL USE ONLY
This bot is for research and educational purposes on Bitcoin testnet networks.

Features:
✅ Real-time wallet discovery alerts
✅ Balance notifications
✅ Testnet research support
✅ Secure and encrypted

For more info: This bot works with Bitcoin Scanner API for educational cryptocurrency research.
```

## 🎯 Bot Commands (U Dir BotFather)

BotFather-ka u dir commands-kan using `/setcommands`:

```
start - Start the bot and get info
help - Show help information
status - Check scanner status
```

## 📱 Sidee Loo Helo Chat ID

Si aad u hesho **CHAT_ID** oo aad ku darto .env:

1. **Fur Telegram app**
2. **Raadi bot-kaaga**: @fadal_awareness_bot
3. **Dir message**: `/start`
4. **Fur browser**: https://api.telegram.org/bot8247674734:AAGhXf-JaNXU0UixUTqotgNYZdPJxASEKxg/getUpdates
5. **Copy chat.id** from response
6. **Ku dar .env file-ka**:
   ```
   CHAT_ID=your_chat_id_here
   ```

## 🔧 Test Bot

Marka aad hesho CHAT_ID, test bot-ka:

```bash
python3 << 'PYTHON'
import requests
import os

BOT_TOKEN = "8247674734:AAGhXf-JaNXU0UixUTqotgNYZdPJxASEKxg"
CHAT_ID = "YOUR_CHAT_ID"  # Replace with your chat ID

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": "✅ Bitcoin Scanner Bot is working! Alerts enabled for testnet research."
}

response = requests.post(url, json=data)
print(response.json())
PYTHON
```

## ✅ Integration Status

- ✅ Bot Token: Added to .env
- ⏳ Chat ID: Waiting (follow steps above)
- ✅ Alert System: Ready
- ✅ Testnet Mode: Active

Once Chat ID is added, bot will send alerts when wallets with balance are found!
