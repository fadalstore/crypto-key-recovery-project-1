import csv
import os
from datetime import datetime
from typing import List, Dict, Any
from config import config


def export_to_csv(data: List[Dict[str, Any]], filename: str = "wallets_found.csv") -> str:
    """
    Export wallet data to CSV file with timestamp
    
    Args:
        data: List of wallet dictionaries with keys: address, private_key, balance
        filename: Base filename for the CSV (default: wallets_found.csv)
    
    Returns:
        Full path to the created CSV file
    """
    if not data:
        return ""
    
    # Create exports directory if it doesn't exist
    os.makedirs(config.CSV_OUTPUT_DIR, exist_ok=True)
    
    # Generate timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    full_name = os.path.join(config.CSV_OUTPUT_DIR, f"{timestamp}_{filename}")
    
    # Define CSV columns
    fieldnames = ["timestamp", "address", "private_key", "balance"]
    
    # Add timestamp to each record
    for record in data:
        if "timestamp" not in record:
            record["timestamp"] = datetime.now().isoformat()
    
    # Write to CSV
    try:
        with open(full_name, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(data)
        
        print(f"✅ CSV exported: {full_name}")
        return full_name
    
    except Exception as e:
        print(f"❌ CSV export failed: {e}")
        return ""
