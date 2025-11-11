#!/usr/bin/env python3
"""
Helper script to generate secure credentials for Bitcoin Scanner
"""

import secrets
import bcrypt

print("=" * 80)
print("🔐 BITCOIN SCANNER - SECURE CREDENTIALS GENERATOR")
print("=" * 80)
print()

# Generate username
username = input("Enter dashboard username (or press Enter for random): ").strip()
if not username:
    username = f"admin_{secrets.token_hex(4)}"
    print(f"Generated username: {username}")

print()

# Generate password
use_random = input("Generate random secure password? (yes/no): ").strip().lower()
if use_random in ['yes', 'y', '']:
    password = secrets.token_urlsafe(16)  # 16 chars is secure enough for bcrypt
    print(f"Generated password: {password}")
    print("⚠️  SAVE THIS PASSWORD - You won't see it again!")
else:
    password = input("Enter your password: ").strip()

print()
print("Hashing password with bcrypt (this may take a few seconds)...")
password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

print()
print("=" * 80)
print("✅ CREDENTIALS GENERATED SUCCESSFULLY")
print("=" * 80)
print()
print("Add these to your environment variables (.env file or Replit Secrets):")
print()
print(f"DASHBOARD_USERNAME={username}")
print(f"DASHBOARD_PASSWORD_HASH={password_hash}")
print()
print("Optional security settings:")
print(f"API_KEY={secrets.token_urlsafe(32)}")
print("USE_TESTNET=true")
print("ENABLE_MAINNET=false")
print("REQUIRE_API_KEY=true")
print()
print("=" * 80)
print()
print("🔒 IMPORTANT: Keep these credentials secure and never commit them to git!")
print("=" * 80)
