# 🔍 Bitcoin Scanner API

A comprehensive Bitcoin wallet scanner that generates random private keys and checks their balances. Features automated scanning, Telegram alerts, CSV exports, cloud backup, and an authenticated web dashboard.

## ⚠️ Disclaimer

This project is for educational and research purposes only. The probability of finding a Bitcoin wallet with balance through random generation is astronomically low (similar to winning the lottery millions of times consecutively). Always obtain proper authorization before accessing any digital assets.

## ✨ Features

### Core Features
- **Random Key Generation** - Generate random Bitcoin private keys and addresses
- **Balance Checking** - Scan addresses for BTC balance using blockchain APIs
- **Multi-Language Seed Phrases** - Generate 12-word mnemonic seeds in multiple languages
- **Test Mode** - Run without external dependencies (local JSON storage, console alerts)

### Storage & Backup
- **MongoDB Integration** - Persistent storage for production use
- **CSV Export** - Automatic timestamped CSV exports of found wallets
- **Storage Manager** - Automatic file rotation with configurable retention (default: 30 days)
- **Google Drive Backup** - Optional cloud backup integration

### Notifications & Monitoring
- **Telegram Alerts** - Real-time notifications when wallets with balance are found
- **Web Dashboard** - Authenticated interface to view results with search and pagination
- **API Endpoints** - RESTful API for programmatic access
- **Automated Scanning** - 24/7 scheduled scanning with APScheduler

### Security
- **HTTP Basic Authentication** - Protected dashboard and API endpoints
- **Configurable Credentials** - Environment-based authentication
- **Secret Management** - Support for Replit Secrets for secure credential storage

## 🚀 Quick Start

### Running on Replit (Recommended)

1. **No configuration needed!** The app runs in **TEST MODE** by default:
   - Uses local JSON file for storage
   - Prints alerts to console
   - All features work out of the box

2. **Start the server:**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 5000
   ```
   The server is already configured to run automatically in Replit.

3. **Access the interface:**
   - Home: `/` - Interactive web interface
   - Dashboard: `/dashboard` - View results (login: admin/admin123)
   - API Docs: `/docs` - Swagger UI documentation

### Running Locally

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server:**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 5000
   ```

3. **Visit** `http://localhost:5000`

## 📚 API Endpoints

### Public Endpoints

- `GET /` - Web interface homepage
- `GET /docs` - Interactive API documentation (Swagger UI)

### Scanning Endpoints

- `GET /seed` - Generate a 12-word seed phrase
  ```bash
  curl http://localhost:5000/seed
  ```

- `GET /scan?batch={number}` - Scan random keys (default: 100)
  ```bash
  curl http://localhost:5000/scan?batch=10
  ```

- `GET /scheduler/status` - Check automated scanner status
  ```bash
  curl http://localhost:5000/scheduler/status
  ```

### Protected Endpoints (Require Authentication)

- `GET /dashboard` - Web dashboard to view found wallets
- `GET /api/wallets?limit={number}` - Get wallets as JSON

**Authentication:**
```bash
curl -u admin:admin123 http://localhost:5000/api/wallets
```

## ⚙️ Configuration

All configuration is done through environment variables. See `.env.example` for complete details.

### Essential Settings

#### Database (Optional)
```bash
MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/dbname
```
Leave empty for TEST MODE (local JSON storage)

#### Telegram Alerts (Optional)
```bash
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
```
Leave empty for console logging

#### Dashboard Security (⚠️ Important!)
```bash
DASHBOARD_USERNAME=admin
DASHBOARD_PASSWORD=admin123  # CHANGE THIS!
```
**Always change default credentials before deployment!**

#### Automated Scanning
```bash
ENABLE_AUTO_SCAN=true           # Enable 24/7 scanning
SCAN_INTERVAL_MINUTES=30        # Scan every 30 minutes
SCAN_BATCH_SIZE=50              # Scan 50 keys per batch
```

#### CSV Export
```bash
CSV_OUTPUT_DIR=exports          # Export directory
CSV_ROTATION_DAYS=30            # Keep files for 30 days
```

#### Google Drive Backup (Optional)
```bash
ENABLE_DRIVE_BACKUP=true
GOOGLE_SERVICE_ACCOUNT_JSON=/path/to/credentials.json
DRIVE_FOLDER_ID=your_folder_id
```

### Using Replit Secrets

For security, use Replit Secrets instead of `.env` file:

1. Click the 🔒 **Secrets** icon in the sidebar
2. Add secrets as key-value pairs
3. They'll be available as environment variables automatically

**Recommended secrets to add:**
- `DASHBOARD_USERNAME` and `DASHBOARD_PASSWORD` (for security)
- `MONGO_URI`, `BOT_TOKEN`, `CHAT_ID` (for production)
- `ENABLE_AUTO_SCAN`, `SCAN_BATCH_SIZE` (for automation)

## 🎯 Usage Modes

### Test Mode (Default)
Perfect for development and testing:
- ✅ No external services required
- ✅ Local JSON file storage (`found_wallets.json`)
- ✅ Console alert logging
- ✅ All features functional
- ✅ CSV exports still work

**How to enable:** Leave `MONGO_URI` and `BOT_TOKEN` empty

### Production Mode
For 24/7 operation:
- ✅ MongoDB Atlas for persistent storage
- ✅ Telegram real-time alerts
- ✅ Automated scheduling
- ✅ Optional Google Drive backup
- ⚠️ Secure credentials required!

**How to enable:**
1. Set `MONGO_URI` to your MongoDB connection string
2. Set `BOT_TOKEN` and `CHAT_ID` for Telegram
3. Change `DASHBOARD_PASSWORD` to a strong value
4. Set `ENABLE_AUTO_SCAN=true`
5. Restart the server

## 📊 Data Storage

### Test Mode Storage
- **File:** `found_wallets.json`
- **Format:** JSON array of wallet objects
- **Location:** Project root directory

### Production Mode Storage
- **Database:** MongoDB Atlas
- **Collection:** `wallets`
- **CSV Exports:** `exports/` directory (timestamped)
- **Cloud Backup:** Google Drive (if enabled)

### CSV Format
```csv
timestamp,address,private_key,balance
2024-01-01T12:00:00,1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa,L5oLkpV...,0.001
```

## 🔐 Security Best Practices

### 1. Change Default Credentials
The default dashboard credentials (`admin`/`admin123`) are **NOT SECURE**:

```bash
# Set in Replit Secrets or .env
DASHBOARD_USERNAME=your_secure_username
DASHBOARD_PASSWORD=your_very_strong_password_123!
```

### 2. Protect Sensitive Data
- Use Replit Secrets for API keys and credentials
- Never commit `.env` file to version control
- Keep `found_wallets.json` and `exports/` directory private
- Secure MongoDB with strong passwords and IP whitelist

### 3. Google Drive Security
- Use service account with minimal permissions
- Store credentials in Replit Secrets
- Set folder permissions to private
- Enable encryption at rest

## 🛠️ Development

### Project Structure
```
bitcoin-scanner/
├── main.py                   # FastAPI app & endpoints
├── scanner.py                # Core scanning logic
├── seed_generator.py         # Seed phrase generation
├── mongo_utils.py            # Database operations
├── telegram_bot.py           # Telegram notifications
├── config.py                 # Configuration management
├── dashboard.py              # Dashboard router
├── scheduler.py              # Automated scanning
├── storage/
│   ├── csv_export.py         # CSV export functionality
│   ├── storage_manager.py    # File rotation & management
│   └── drive_client.py       # Google Drive backup
├── templates/
│   └── dashboard.html        # Dashboard HTML template
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
└── README.md                 # This file
```

### Adding Dependencies
```bash
# Using pip
pip install package_name

# Using upm (Replit's package manager)
upm add package_name

# Add to requirements.txt
echo "package_name" >> requirements.txt
```

### Running Tests
Create a test script:
```python
import requests

# Test scan endpoint
response = requests.get("http://localhost:5000/scan?batch=5")
print(response.json())
```

## 📱 Telegram Setup

1. **Create a bot:**
   - Message [@BotFather](https://t.me/BotFather) on Telegram
   - Send `/newbot` and follow instructions
   - Copy the bot token

2. **Get your Chat ID:**
   - Message [@userinfobot](https://t.me/userinfobot)
   - Copy your chat ID (numeric)

3. **Configure:**
   ```bash
   BOT_TOKEN=1234567890:ABCdefGHI_your_token_here
   CHAT_ID=123456789
   ```

4. **Test:**
   - Start a scan
   - Wait for a result
   - Check Telegram for alert

## ☁️ Google Drive Setup (Optional)

1. **Create service account:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create project → Enable Drive API
   - Create service account
   - Download JSON key file

2. **Get folder ID:**
   - Create folder in Google Drive
   - Open folder → Copy ID from URL
   - Example: `drive.google.com/drive/folders/YOUR_FOLDER_ID`

3. **Configure:**
   ```bash
   ENABLE_DRIVE_BACKUP=true
   GOOGLE_SERVICE_ACCOUNT_JSON=/path/to/key.json
   DRIVE_FOLDER_ID=your_folder_id_here
   ```

## 🚀 Deployment

### Deploying on Replit

1. **Configure production secrets** (🔒 Secrets tab):
   - `MONGO_URI`
   - `BOT_TOKEN` and `CHAT_ID`
   - `DASHBOARD_PASSWORD` (strong password!)
   - `ENABLE_AUTO_SCAN=true`

2. **Click "Publish"** button to deploy

3. **Monitor logs** to ensure everything works

### Deploying Elsewhere

The app is a standard FastAPI application and can be deployed to:
- Heroku
- AWS (EC2, Lambda, ECS)
- Google Cloud (Cloud Run, App Engine)
- DigitalOcean
- Any VPS with Python support

**Deployment command:**
```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

## 📈 Performance Tuning

### Batch Size
- Small batch (10-50): Lower resource usage, slower
- Large batch (100-500): Higher resource usage, faster
- Recommended: 50-100 for balanced performance

### Scan Interval
- Short interval (5-15 min): More frequent scans, higher cost
- Long interval (30-60 min): Less frequent, lower cost
- Recommended: 30 minutes for production

### Concurrent Scans
- Default: 1 (safest)
- Higher values possible with more resources
- Monitor CPU and memory usage

## 🔧 Troubleshooting

### Server Won't Start
```bash
# Check if port is in use
pkill -f uvicorn

# Restart server
uvicorn main:app --host 0.0.0.0 --port 5000
```

### Dashboard Shows "Not Authenticated"
- Browser didn't show login prompt
- Try accessing in incognito/private mode
- Or use curl: `curl -u admin:admin123 http://localhost:5000/dashboard`

### Automatic Scanning Not Working
Check environment variables:
```bash
# Should return "true"
echo $ENABLE_AUTO_SCAN

# Should return numbers
echo $SCAN_INTERVAL_MINUTES
echo $SCAN_BATCH_SIZE
```

Fix invalid values:
- `ENABLE_AUTO_SCAN` must be exactly `true` (lowercase)
- `SCAN_INTERVAL_MINUTES` must be a number (e.g., `30`)
- `SCAN_BATCH_SIZE` must be a number (e.g., `50`)

### CSV Files Not Being Created
- Check `CSV_OUTPUT_DIR` exists and is writable
- Verify scans are finding wallets (check console logs)
- Files are only created when wallets with balance are found

## 📝 License

This project is for educational purposes. Use responsibly and at your own risk.

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional blockchain API providers
- Enhanced error handling
- Performance optimizations
- Additional export formats
- UI improvements

## 📞 Support

- Check `replit.md` for project-specific notes
- View API docs at `/docs` endpoint
- Check logs for error messages
- Review `.env.example` for configuration

## 🎓 Learning Resources

- [Bitcoin Development](https://bitcoin.org/en/developer-documentation)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Bitcoinlib Library](https://github.com/1200wd/bitcoinlib)
- [APScheduler Guide](https://apscheduler.readthedocs.io/)

---

**Made with ❤️ using FastAPI and Python**
