# Bitcoin Scanner API

## Maxuu Yahay Mashruucan?

Mashruucan waa **Bitcoin Wallet Scanner** oo Random Bitcoin private keys abuuraya oo baaraya haddii lacag ay ku jirto addresses-ka.

## Features (Sifooyin)

1. **Random Key Generation** - Abuurista Bitcoin private keys iyo addresses random ah
2. **Balance Checking** - Baarista balance-ka addressyada
3. **Alert System** - Telegram alerts (ama console haddii test mode)
4. **Data Storage** - MongoDB storage (ama JSON file haddii test mode)
5. **Seed Phrase Generator** - Abuurista 12-word mnemonic seed phrases

## Project Structure

```
├── main.py              # FastAPI web server + endpoints
├── scanner.py           # Core scanning logic
├── seed_generator.py    # Seed phrase generation
├── telegram_bot.py      # Telegram notifications
├── mongo_utils.py       # Database storage
└── requirements.txt     # Python dependencies
```

## Endpoints

### Web Interface
- `GET /` - Simple web interface for testing

### API Endpoints
- `GET /seed` - Generate new 12-word seed phrase
- `GET /scan?batch={number}` - Scan random keys (default: 100)
- `GET /docs` - FastAPI auto-generated API documentation

## Test Mode

Mashruucan wuxuu shaqeeyaa **TEST MODE** haddii secrets la'aan:
- ✅ Local JSON file storage (halkii MongoDB)
- ✅ Console logging (halkii Telegram alerts)
- ✅ Dhammaan endpoints-ka way shaqeynayaan

## Production Mode

Si loo isticmaalo production mode, waxaa loo baahan yahay environment variables:
- `MONGO_URI` - MongoDB connection string
- `BOT_TOKEN` - Telegram bot token
- `CHAT_ID` - Telegram chat ID

## Recent Changes (Nov 7, 2025)

- ✅ Ku daray test mode functionality
- ✅ JSON file storage halkii MongoDB (test mode)
- ✅ Console alerts halkii Telegram (test mode)
- ✅ Ku daray web interface (home page)
- ✅ Auto-detect mode based on secrets availability

## Installation

```bash
# Dependencies-ka way ku jiraan already
uv pip install -r requirements.txt
```

## Running

```bash
# Server automatically runs on port 5000
uvicorn main:app --host 0.0.0.0 --port 5000
```

## Notes

- Bitcoin address scanning waa extremely rare in finding balances
- Test mode waa safe oo local
- Production mode needs proper MongoDB iyo Telegram setup
