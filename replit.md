# Bitcoin Scanner API

## Maxuu Yahay Mashruucan?

Mashruucan waa **Bitcoin Wallet Scanner** oo Random Bitcoin private keys abuuraya oo baaraya haddii lacag ay ku jirto addresses-ka. Waa mashruuc guul leh oo si buuxda u shaqeynaya oo leh dhammaan features-ka muhiimka ah.

## ✅ Current Status (November 7, 2025)

**Server:** ✅ Running successfully on port 5000  
**Mode:** TEST MODE (safe for development)  
**All Features:** Fully functional  
**Documentation:** Complete with README.md and .env.example  
**Deployment:** Ready to publish  

## Features (Sifooyin)

1. **Random Key Generation** ✅ - Abuurista Bitcoin private keys iyo addresses random ah
2. **Balance Checking** ✅ - Baarista balance-ka addressyada
3. **Alert System** ✅ - Telegram alerts (ama console haddii test mode)
4. **Data Storage** ✅ - MongoDB storage (ama JSON file haddii test mode)
5. **Seed Phrase Generator** ✅ - Abuurista 12-word mnemonic seed phrases (multi-language support)
6. **CSV Export** 📊 ✅ - Automatic export of found wallets to CSV files with timestamp
7. **Storage Manager** 📁 ✅ - Local file storage with automatic rotation (30-day retention)
8. **Google Drive Backup** ☁️ ✅ - Optional cloud backup integration
9. **Dashboard** 🖥️ ✅ - Authenticated web interface to view found wallets
10. **Automated Scanning** ⏰ ✅ - 24/7 scheduled scanning with APScheduler
11. **Health Check** 🏥 ✅ - `/health` endpoint to verify all systems
12. **Test Endpoint** 🧪 ✅ - `/test` endpoint to verify scanner functionality

## Project Structure

```
├── main.py                   # FastAPI web server + endpoints
├── scanner.py                # Core scanning logic
├── seed_generator.py         # Seed phrase generation (multi-language)
├── telegram_bot.py           # Telegram notifications
├── mongo_utils.py            # Database storage
├── config.py                 # Centralized configuration
├── dashboard.py              # Dashboard router with auth
├── scheduler.py              # Automated scanning scheduler
├── storage/
│   ├── csv_export.py         # CSV export functionality
│   ├── storage_manager.py    # File rotation and management
│   └── drive_client.py       # Google Drive backup (optional)
├── templates/
│   └── dashboard.html        # Dashboard HTML template
├── requirements.txt          # Python dependencies
└── .env.example              # Environment variables template
```

## Endpoints

### Web Interface
- `GET /` - Simple web interface for testing all endpoints

### API Endpoints
- `GET /seed` - Generate new 12-word seed phrase
- `GET /scan?batch={number}` - Scan random keys (default: 100)
- `GET /dashboard` - View found wallets dashboard (requires auth: admin/admin123)
- `GET /api/wallets` - Get found wallets as JSON (requires auth)
- `GET /scheduler/status` - Check automated scanning status
- `GET /health` - System health check and configuration status
- `GET /test` - Test scanner functionality with single key
- `GET /docs` - FastAPI auto-generated API documentation

## Test Mode

Mashruucan wuxuu shaqeeyaa **TEST MODE** haddii secrets la'aan:
- ✅ Local JSON file storage (halkii MongoDB)
- ✅ Console logging (halkii Telegram alerts)
- ✅ Dhammaan endpoints-ka way shaqeynayaan

## Configuration

### Environment Variables

All configuration is managed via environment variables. See `.env.example` for full details:

**Core Features:**
- `MONGO_URI` - MongoDB connection string (optional, test mode if empty)
- `BOT_TOKEN` - Telegram bot token (optional)
- `CHAT_ID` - Telegram chat ID (optional)

**CSV & Storage:**
- `CSV_OUTPUT_DIR` - Directory for CSV exports (default: exports)
- `CSV_ROTATION_DAYS` - Days to keep old CSVs (default: 30)

**Google Drive (Optional):**
- `ENABLE_DRIVE_BACKUP` - Enable Google Drive backup (default: false)
- `GOOGLE_SERVICE_ACCOUNT_JSON` - Service account credentials
- `DRIVE_FOLDER_ID` - Target folder ID

**Dashboard:**
- `DASHBOARD_USERNAME` - Dashboard username (default: admin)
- `DASHBOARD_PASSWORD` - Dashboard password (⚠️ CHANGE DEFAULT!)

**Automated Scanning:**
- `ENABLE_AUTO_SCAN` - Enable 24/7 scanning (default: false)
- `SCAN_INTERVAL_MINUTES` - Minutes between scans (default: 30)
- `SCAN_BATCH_SIZE` - Keys per scan (default: 50)
- `MAX_CONCURRENT_SCANS` - Max parallel jobs (default: 1)
- `ERROR_THRESHOLD` - Errors before stopping (default: 5)

## Recent Changes (Nov 7, 2025)

### Version 2.1 - Production Ready Release
- ✅ **Health Check Endpoint** - System monitoring and status verification
- ✅ **Test Endpoint** - Quick scanner functionality verification
- ✅ **Deployment Configuration** - Ready for Replit publishing
- ✅ **Comprehensive README** - Full documentation with examples
- ✅ **Error Handling** - Safe config parsing for invalid environment variables
- ✅ **Documentation Complete** - README.md, .env.example, replit.md

### Version 2.0 - Full Feature Suite
- ✅ **CSV Export System** - Automatic export of found wallets with timestamps
- ✅ **Storage Manager** - File rotation and retention management
- ✅ **Dashboard** - Authenticated web UI with pagination and search
- ✅ **Automated Scanning** - APScheduler for 24/7 operation
- ✅ **Google Drive Backup** - Optional cloud storage integration
- ✅ **Multi-language Seeds** - Support for Spanish, French, etc.
- ✅ **Centralized Config** - Environment-based configuration
- ✅ **Security Enhancements** - Auth warnings and secure credential handling

### Version 1.0 - Initial Release
- ✅ Test mode functionality
- ✅ JSON file storage (test mode)
- ✅ Console alerts (test mode)
- ✅ Web interface (home page)
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

## Security Notes

⚠️ **IMPORTANT SECURITY WARNINGS:**

1. **Dashboard Credentials**: Default username/password is `admin`/`admin123`
   - **CHANGE IMMEDIATELY** before any public deployment
   - Set `DASHBOARD_USERNAME` and `DASHBOARD_PASSWORD` environment variables
   - Use strong, unique passwords

2. **Private Keys**: Found wallet private keys are stored in:
   - CSV files (timestamped in `exports/` directory)
   - MongoDB (if configured)
   - Console logs (in test mode)
   - **Protect these files and logs carefully!**

3. **Google Drive**: If enabled, ensure:
   - Service account has minimal permissions
   - Target folder is private
   - Credentials are stored securely (use Replit Secrets)

## Usage Tips

### For Testing (Safe, Local)
- No configuration needed - just run!
- Results saved in `exports/` folder
- No external services required

### For Production (24/7 Operation)
1. Set MongoDB credentials (`MONGO_URI`)
2. Set Telegram credentials (`BOT_TOKEN`, `CHAT_ID`)
3. **Change dashboard password!** (`DASHBOARD_PASSWORD`)
4. Enable automated scanning (`ENABLE_AUTO_SCAN=true`)
5. Optional: Enable Google Drive backup

### Viewing Results
- **Dashboard**: Visit `/dashboard` (login: admin/admin123 by default)
- **CSV Files**: Check `exports/` directory
- **API**: Use `/api/wallets` endpoint (requires auth)

## Notes

- Bitcoin address scanning is extremely rare in finding balances
- Test mode is safe and completely local
- CSV files are automatically rotated after 30 days
- Scheduler respects error thresholds for safety
- All sensitive data should be stored via environment variables or Replit Secrets
