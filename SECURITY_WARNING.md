# 🚨 CRITICAL SECURITY NOTICE

## ⚠️ STORED PRIVATE KEYS DETECTED

This scanner may have stored private keys in the following locations:

- **CSV Files**: `exports/*.csv`
- **JSON Files**: `results.json`
- **Database**: MongoDB collection `crypto_recovery.results`

## 🔒 IMMEDIATE ACTION REQUIRED

### 1. Delete All Stored Private Keys

```bash
# Delete CSV exports
rm -rf exports/*.csv

# Delete JSON results
rm -f results.json

# If using MongoDB, clear the collection:
# mongosh and run: db.results.drop()
```

### 2. Security Best Practices Going Forward

- **NEVER store private keys** on the server
- **NEVER log private keys** in any way
- Use **client-side generation** only (`/client-seed-generator`)
- Operate on **TESTNET** only for research
- Follow all legal and ethical guidelines

### 3. Legal Reminder

Attempting to access wallets you do not own is **ILLEGAL** and may result in:
- Criminal prosecution
- Imprisonment
- Substantial fines
- Permanent criminal record

## ✅ Updated Security Measures

This application now includes:

✅ **Client-side seed generation** - seeds never touch the server
✅ **Password hashing** with bcrypt
✅ **Rate limiting** on sensitive endpoints
✅ **API key authentication** required
✅ **HTTPS security headers** (HSTS, CSP, etc.)
✅ **Testnet mode** as default
✅ **Legal disclaimers** and Terms of Service
✅ **Input validation** and sanitization

## 📚 Read More

- [Terms of Service](/terms)
- [Client-Side Seed Generator](/client-seed-generator)

---

**Last Updated**: November 11, 2025
