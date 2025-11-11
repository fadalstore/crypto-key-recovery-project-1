# Bitcoin Scanner API - SECURED & LEGAL COMPLIANT

## 🚨 CRITICAL UPDATE (November 11, 2025)

**MAJOR SECURITY OVERHAUL COMPLETED** - This project has been completely hardened with enterprise-grade security features and legal compliance measures.

## Maxuu Yahay Mashruucan?

Mashruucan waa **Bitcoin Wallet Scanner** oo TESTNET keliya ku shaqeeya - wuxuu ku qorsheysan yahay **cilmi baaris iyo waxbarasho keliya**. Wuxuu leeyahay dhammaan amniga sare iyo legal compliance.

## ✅ Current Status (November 11, 2025)

**Server:** ⚠️ Requires secure credentials to start
**Mode:** TESTNET ONLY (safe for research - mainnet DISABLED by default)  
**Security:** ✅ Enterprise-grade hardening complete
**Authentication:** ✅ Bcrypt password hashing required
**Legal Compliance:** ✅ Full disclaimers and Terms of Service
**Client-Side Seeds:** ✅ Seeds never touch server
**Deployment:** ⚠️ Requires credential setup before publishing

## 🔒 MAJOR SECURITY IMPROVEMENTS

### ✅ Authentication & Authorization
- **Bcrypt password hashing** - No more plaintext passwords
- **Mandatory credentials** - Application won't start without secure auth
- **API key authentication** - All sensitive endpoints protected
- **Constant-time comparisons** - Prevents timing attacks

### ✅ Network Security
- **HTTPS Headers** - HSTS, CSP, X-Frame-Options, etc.
- **Rate limiting** - 5 requests/minute on scan endpoints
- **Input validation** - Protection against injection attacks
- **Security middleware** - Defense in depth

### ✅ Data Protection
- **Client-side seed generation** - Seeds NEVER touch server
- **Testnet-first mode** - Mainnet disabled by default
- **No plaintext key storage** - Server-side seed generation disabled
- **Secure credential generation** - Helper script provided

### ✅ Legal Compliance
- **Terms of Service** - Full legal disclaimer at `/terms`
- **Educational purpose** - Clear research/educational only messaging
- **Liability protection** - Comprehensive legal warnings
- **Ethical guidelines** - Best practices documented  

## Features (Sifooyin)

### 🔒 Security Features (NEW!)
1. **Bcrypt Authentication** 🔐 ✅ - Password hashing with bcrypt
2. **Rate Limiting** 🚦 ✅ - SlowAPI protection on all endpoints
3. **Security Headers** 🛡️ ✅ - HSTS, CSP, X-Frame-Options, etc.
4. **API Key Protection** 🔑 ✅ - Required for scan endpoints
5. **Client-Side Seeds** 💻 ✅ - Browser-based seed generation
6. **Input Validation** ✅ - Sanitization and validation
7. **Testnet Mode** 🧪 ✅ - Default safe mode (mainnet disabled)

### 📋 Legal & Compliance (NEW!)
8. **Terms of Service** ⚖️ ✅ - Full legal disclaimer page
9. **Usage Warnings** ⚠️ ✅ - Clear educational purpose messaging
10. **Credential Generator** 🔧 ✅ - Helper script for secure setup

### 🔍 Core Features
11. **Random Key Generation** ✅ - Bitcoin key generation (testnet)
12. **Balance Checking** ✅ - Address balance scanning
13. **Alert System** ✅ - Telegram/console notifications
14. **Data Storage** ✅ - MongoDB/JSON storage
15. **CSV Export** 📊 ✅ - Automatic CSV exports
16. **Storage Manager** 📁 ✅ - File rotation (30-day retention)
17. **Dashboard** 🖥️ ✅ - Secure authenticated interface
18. **Automated Scanning** ⏰ ✅ - Scheduled scanning
19. **Health Check** 🏥 ✅ - System status endpoint

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

### Public Pages
- `GET /` - Home page with links and warnings
- `GET /client-seed-generator` - 🔒 CLIENT-SIDE seed generator (100% secure)
- `GET /terms` - Terms of Service and Legal Disclaimer
- `GET /docs` - FastAPI auto-generated API documentation

### Protected Endpoints (Require Authentication)
- `GET /dashboard` - View found wallets (HTTP Basic Auth with bcrypt)
- `GET /api/wallets` - Get wallets as JSON (HTTP Basic Auth)

### API Endpoints (Require API Key)
- `GET /scan?batch={number}` - Scan keys (rate limited: 5/min, max batch: 100)
- `GET /seed` - ❌ DEPRECATED - Use client-side generator instead

### Status & Monitoring
- `GET /scheduler/status` - Check automated scanning status
- `GET /health` - System health check and configuration
- `GET /test` - Test scanner functionality

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

## Recent Changes

### Version 3.0 - SECURITY & LEGAL OVERHAUL (November 11, 2025)

🔒 **CRITICAL SECURITY UPDATE** - Complete security hardening and legal compliance:

**Authentication & Authorization:**
- ✅ Bcrypt password hashing (no more plaintext)
- ✅ Mandatory credentials requirement
- ✅ API key authentication for protected endpoints
- ✅ Constant-time credential comparison
- ✅ HTTP Basic Auth for dashboard

**Network Security:**
- ✅ HTTPS security headers (HSTS, CSP, X-Frame-Options, etc.)
- ✅ Rate limiting with SlowAPI (5 req/min on scan)
- ✅ Input validation and sanitization
- ✅ Security middleware

**Data Protection:**
- ✅ Client-side seed generation (browser only)
- ✅ Server-side seed generation DISABLED
- ✅ Testnet-first mode (mainnet disabled by default)
- ✅ No plaintext key storage on server

**Legal Compliance:**
- ✅ Terms of Service page (`/terms`)
- ✅ Legal disclaimers throughout
- ✅ Educational purpose warnings
- ✅ Liability protection documentation

**Developer Tools:**
- ✅ Secure credential generator script
- ✅ .env.example template
- ✅ .gitignore for sensitive files
- ✅ SECURITY_WARNING.md guide

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

## 🚨 CRITICAL SETUP REQUIRED

### Before Running the Application

**The application WILL NOT START without secure credentials!**

1. **Generate Secure Credentials**
   ```bash
   python generate_credentials.py
   ```
   This will generate:
   - Secure username
   - Random password (24+ characters)
   - Bcrypt password hash
   - API key

2. **Set Environment Variables**
   Add to Replit Secrets or `.env` file:
   ```env
   DASHBOARD_USERNAME=your_generated_username
   DASHBOARD_PASSWORD_HASH=your_bcrypt_hash
   API_KEY=your_generated_api_key
   USE_TESTNET=true
   ENABLE_MAINNET=false
   REQUIRE_API_KEY=true
   ```

3. **Security Best Practices**
   - ✅ Use the credentials generator script
   - ✅ Store credentials in Replit Secrets (not in code)
   - ✅ Use client-side seed generator only
   - ✅ Keep testnet mode enabled
   - ✅ Never commit credentials to git
   - ⚠️ Read the Terms of Service at `/terms`

## Security Notes

⚠️ **SECURITY REQUIREMENTS:**

1. **Authentication**: 
   - **MANDATORY bcrypt hashed passwords** - No plaintext allowed
   - Application enforces credentials at startup
   - Use `generate_credentials.py` to create secure credentials

2. **Seed Generation**:
   - **Server-side generation DISABLED** for security
   - Use `/client-seed-generator` - 100% browser-based
   - Seeds never touch the server or network

3. **Network Mode**:
   - **Testnet mode is DEFAULT** - Safe for research
   - Mainnet is DISABLED unless explicitly enabled
   - Warning shown if mainnet is activated

4. **Rate Limiting**:
   - Scan endpoint: 5 requests per minute
   - Prevents abuse and DoS attacks
   - API key required for all sensitive operations

5. **Legal Compliance**:
   - Read `/terms` before using
   - For educational/research use ONLY
   - Unauthorized wallet access is ILLEGAL

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
