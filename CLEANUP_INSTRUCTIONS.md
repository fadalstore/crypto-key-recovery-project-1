# 🚨 CLEANUP INSTRUCTIONS - READ BEFORE FIRST RUN

## ⚠️ WARNING: Private Keys May Be Stored

If this scanner was previously run, **private keys may be stored** in:

1. **CSV Files** - `exports/*.csv`
2. **JSON Files** - `results.json`
3. **Database** - MongoDB collection `crypto_recovery.results`
4. **Logs** - Console output logs

## 🗑️ IMMEDIATE CLEANUP REQUIRED

### Step 1: Delete All Stored Data

```bash
# Delete CSV exports (if they exist)
rm -rf exports/

# Delete JSON results
rm -f results.json

# Clear logs
rm -f *.log
```

### Step 2: Clean Database (if using MongoDB)

```bash
# Connect to MongoDB and run:
mongosh "$MONGO_URI"
> use crypto_recovery
> db.results.drop()
> exit
```

### Step 3: Verify Cleanup

```bash
# Check that files are deleted
ls -la exports/ 2>/dev/null
ls -la results.json 2>/dev/null
```

## ✅ AFTER CLEANUP

Once you've cleaned up old data:

1. **Generate secure credentials**:
   ```bash
   python generate_credentials.py
   ```

2. **Set environment variables** (Replit Secrets or .env):
   ```env
   DASHBOARD_USERNAME=your_generated_username
   DASHBOARD_PASSWORD_HASH=your_bcrypt_hash
   API_KEY=your_api_key
   USE_TESTNET=true
   ENABLE_MAINNET=false
   ```

3. **Start the server**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 5000
   ```

4. **Use ONLY client-side seed generation**:
   - Visit `/client-seed-generator`
   - Seeds are generated in your browser only
   - NEVER use the old `/seed` endpoint

## 🔒 SECURITY GOING FORWARD

- ✅ **Client-side only** - Use `/client-seed-generator` 
- ✅ **Testnet mode** - Keep `USE_TESTNET=true`
- ✅ **No key storage** - Server never sees or stores seeds
- ✅ **Read Terms** - Visit `/terms` for legal information
- ⚠️ **Educational only** - Research on testnet only

## 📋 LEGAL REMINDER

**This tool is for EDUCATIONAL and RESEARCH purposes ONLY.**

- Unauthorized wallet access is **ILLEGAL**
- Use **testnet only** for research
- Read full legal disclaimer at `/terms`
- You are responsible for compliance with all laws

---

For more information, see:
- `SECURITY_WARNING.md`
- `/terms` endpoint
- `replit.md` documentation
