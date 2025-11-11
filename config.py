import os
import secrets
import bcrypt
from typing import Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def hash_password(password: str) -> str:
    """Hash a password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def verify_password(password: str, hashed: str) -> bool:
    """Verify a password against a bcrypt hash"""
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    except Exception:
        return False


def safe_int(value: str, default: int) -> int:
    """Safely convert string to int with fallback to default"""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def safe_bool(value: str, default: bool = False) -> bool:
    """Safely convert string to bool"""
    if not value:
        return default
    return value.lower() in ("true", "1", "yes", "on")


def generate_secure_password() -> str:
    """Generate a cryptographically secure random password"""
    return secrets.token_urlsafe(32)


class Config(BaseModel):
    """Centralized configuration management"""
    
    # Database
    MONGO_URI: Optional[str] = Field(default_factory=lambda: os.getenv("MONGO_URI"))
    
    # Telegram
    BOT_TOKEN: Optional[str] = Field(default_factory=lambda: os.getenv("BOT_TOKEN"))
    CHAT_ID: Optional[str] = Field(default_factory=lambda: os.getenv("CHAT_ID"))
    
    # CSV Export
    CSV_OUTPUT_DIR: str = Field(default_factory=lambda: os.getenv("CSV_OUTPUT_DIR", "exports"))
    CSV_ROTATION_DAYS: int = Field(default_factory=lambda: safe_int(os.getenv("CSV_ROTATION_DAYS", "30"), 30))
    
    # Google Drive Backup (Optional)
    ENABLE_DRIVE_BACKUP: bool = Field(default_factory=lambda: safe_bool(os.getenv("ENABLE_DRIVE_BACKUP", "false")))
    GOOGLE_SERVICE_ACCOUNT_JSON: Optional[str] = Field(default_factory=lambda: os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON"))
    DRIVE_FOLDER_ID: Optional[str] = Field(default_factory=lambda: os.getenv("DRIVE_FOLDER_ID"))
    
    # Dashboard Authentication
    DASHBOARD_USERNAME: str = Field(default_factory=lambda: os.getenv("DASHBOARD_USERNAME"))
    DASHBOARD_PASSWORD_HASH: Optional[str] = Field(default_factory=lambda: os.getenv("DASHBOARD_PASSWORD_HASH"))
    
    # Security
    USE_TESTNET: bool = Field(default_factory=lambda: safe_bool(os.getenv("USE_TESTNET", "true")))
    ENABLE_MAINNET: bool = Field(default_factory=lambda: safe_bool(os.getenv("ENABLE_MAINNET", "false")))
    REQUIRE_API_KEY: bool = Field(default_factory=lambda: safe_bool(os.getenv("REQUIRE_API_KEY", "true")))
    API_KEY: Optional[str] = Field(default_factory=lambda: os.getenv("API_KEY"))
    
    def __init__(self, **data):
        super().__init__(**data)
        
        # CRITICAL: Enforce authentication
        if not self.DASHBOARD_USERNAME or not self.DASHBOARD_PASSWORD_HASH:
            print("\n" + "="*80)
            print("🚨 CRITICAL SECURITY ERROR: No authentication credentials set!")
            print("   ")
            print("   The application REQUIRES secure credentials to run.")
            print("   ")
            print("   TO GENERATE SECURE CREDENTIALS:")
            print("   1. Run: python generate_credentials.py")
            print("   2. Copy output to Replit Secrets or .env file")
            print("   ")
            print("   OR manually with Python:")
            print("   >>> import bcrypt, secrets")
            print("   >>> password = secrets.token_urlsafe(16)")
            print("   >>> bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')")
            print("   ")
            print("   APPLICATION WILL NOT START WITHOUT CREDENTIALS!")
            print("="*80 + "\n")
            raise ValueError("Missing required authentication credentials: DASHBOARD_USERNAME and DASHBOARD_PASSWORD_HASH")
        
        # Warn if mainnet is enabled
        if self.ENABLE_MAINNET and not self.USE_TESTNET:
            print("\n" + "="*80)
            print("⚠️  WARNING: MAINNET MODE ENABLED!")
            print("   ")
            print("   You are running in MAINNET mode. This is DANGEROUS and may")
            print("   have LEGAL CONSEQUENCES. Use TESTNET mode for research.")
            print("   ")
            print("   To use testnet: Set USE_TESTNET=true")
            print("="*80 + "\n")
    
    # Automated Scanning
    ENABLE_AUTO_SCAN: bool = Field(default_factory=lambda: safe_bool(os.getenv("ENABLE_AUTO_SCAN", "false")))
    SCAN_INTERVAL_MINUTES: int = Field(default_factory=lambda: safe_int(os.getenv("SCAN_INTERVAL_MINUTES", "30"), 30))
    SCAN_BATCH_SIZE: int = Field(default_factory=lambda: safe_int(os.getenv("SCAN_BATCH_SIZE", "50"), 50))
    MAX_CONCURRENT_SCANS: int = Field(default_factory=lambda: safe_int(os.getenv("MAX_CONCURRENT_SCANS", "1"), 1))
    ERROR_THRESHOLD: int = Field(default_factory=lambda: safe_int(os.getenv("ERROR_THRESHOLD", "5"), 5))
    
    # Test Mode Detection
    @property
    def is_test_mode(self) -> bool:
        """Check if running in test mode (no MongoDB/Telegram)"""
        return not self.MONGO_URI
    
    @property
    def has_telegram(self) -> bool:
        """Check if Telegram is configured"""
        return bool(self.BOT_TOKEN and self.CHAT_ID)
    
    @property
    def has_drive_backup(self) -> bool:
        """Check if Google Drive backup is enabled and configured"""
        return self.ENABLE_DRIVE_BACKUP and bool(self.GOOGLE_SERVICE_ACCOUNT_JSON)


# Global config instance
config = Config()
