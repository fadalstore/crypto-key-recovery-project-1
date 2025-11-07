import os
from typing import Optional
from pydantic import BaseModel, Field


class Config(BaseModel):
    """Centralized configuration management"""
    
    # Database
    MONGO_URI: Optional[str] = Field(default_factory=lambda: os.getenv("MONGO_URI"))
    
    # Telegram
    BOT_TOKEN: Optional[str] = Field(default_factory=lambda: os.getenv("BOT_TOKEN"))
    CHAT_ID: Optional[str] = Field(default_factory=lambda: os.getenv("CHAT_ID"))
    
    # CSV Export
    CSV_OUTPUT_DIR: str = Field(default_factory=lambda: os.getenv("CSV_OUTPUT_DIR", "exports"))
    CSV_ROTATION_DAYS: int = Field(default_factory=lambda: int(os.getenv("CSV_ROTATION_DAYS", "30")))
    
    # Google Drive Backup (Optional)
    ENABLE_DRIVE_BACKUP: bool = Field(default_factory=lambda: os.getenv("ENABLE_DRIVE_BACKUP", "false").lower() == "true")
    GOOGLE_SERVICE_ACCOUNT_JSON: Optional[str] = Field(default_factory=lambda: os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON"))
    DRIVE_FOLDER_ID: Optional[str] = Field(default_factory=lambda: os.getenv("DRIVE_FOLDER_ID"))
    
    # Dashboard Authentication
    DASHBOARD_USERNAME: str = Field(default_factory=lambda: os.getenv("DASHBOARD_USERNAME", "admin"))
    DASHBOARD_PASSWORD: str = Field(default_factory=lambda: os.getenv("DASHBOARD_PASSWORD", "admin123"))
    
    # Automated Scanning
    ENABLE_AUTO_SCAN: bool = Field(default_factory=lambda: os.getenv("ENABLE_AUTO_SCAN", "false").lower() == "true")
    SCAN_INTERVAL_MINUTES: int = Field(default_factory=lambda: int(os.getenv("SCAN_INTERVAL_MINUTES", "30")))
    SCAN_BATCH_SIZE: int = Field(default_factory=lambda: int(os.getenv("SCAN_BATCH_SIZE", "50")))
    MAX_CONCURRENT_SCANS: int = Field(default_factory=lambda: int(os.getenv("MAX_CONCURRENT_SCANS", "1")))
    ERROR_THRESHOLD: int = Field(default_factory=lambda: int(os.getenv("ERROR_THRESHOLD", "5")))
    
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
