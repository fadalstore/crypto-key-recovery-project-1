import os
import glob
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from config import config
from .csv_export import export_to_csv


class StorageManager:
    """Manage local CSV storage with rotation and optional cloud backup"""
    
    def __init__(self):
        self.output_dir = config.CSV_OUTPUT_DIR
        os.makedirs(self.output_dir, exist_ok=True)
    
    def persist_results(self, results: List[Dict[str, Any]]) -> Optional[str]:
        """
        Persist scan results to CSV and optionally upload to cloud
        
        Args:
            results: List of wallet data dictionaries
        
        Returns:
            Path to created CSV file, or None if no results
        """
        if not results:
            return None
        
        # Export to CSV
        csv_path = export_to_csv(results)
        
        if not csv_path:
            return None
        
        # Clean up old files
        self.rotate_old_files()
        
        # Optional: Upload to Google Drive
        if config.has_drive_backup:
            try:
                from .drive_client import upload_to_drive
                upload_to_drive(csv_path)
            except ImportError:
                print("⚠️  Google Drive backup not available (dependencies not installed)")
            except Exception as e:
                print(f"⚠️  Google Drive upload failed: {e}")
        
        return csv_path
    
    def rotate_old_files(self):
        """Remove CSV files older than configured retention period"""
        try:
            cutoff_date = datetime.now() - timedelta(days=config.CSV_ROTATION_DAYS)
            pattern = os.path.join(self.output_dir, "*.csv")
            
            deleted_count = 0
            for filepath in glob.glob(pattern):
                file_time = datetime.fromtimestamp(os.path.getmtime(filepath))
                if file_time < cutoff_date:
                    os.remove(filepath)
                    deleted_count += 1
            
            if deleted_count > 0:
                print(f"🗑️  Rotated {deleted_count} old CSV file(s)")
        
        except Exception as e:
            print(f"⚠️  File rotation failed: {e}")
    
    def get_all_results(self) -> List[Dict[str, Any]]:
        """
        Read all CSV files and return combined results
        
        Returns:
            List of all wallet records from all CSV files
        """
        import csv
        
        results = []
        pattern = os.path.join(self.output_dir, "*.csv")
        
        for filepath in sorted(glob.glob(pattern), reverse=True):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    results.extend(list(reader))
            except Exception as e:
                print(f"⚠️  Failed to read {filepath}: {e}")
        
        return results


# Global storage manager instance
storage_manager = StorageManager()
