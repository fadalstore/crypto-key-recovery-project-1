"""
Automated scanning scheduler using APScheduler
"""

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime
from config import config
from scanner import scan_keys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global scheduler instance
scheduler = AsyncIOScheduler()

# Error counter for safety
error_count = 0
MAX_ERRORS = config.ERROR_THRESHOLD


def scan_job():
    """Background job that runs the scanner"""
    global error_count
    
    try:
        logger.info(f"🔄 Starting automated scan at {datetime.now()}")
        
        # Run scan with configured batch size
        results = scan_keys(batch_size=config.SCAN_BATCH_SIZE)
        
        if results:
            logger.info(f"💰 Found {len(results)} wallets with balance!")
        else:
            logger.info(f"✅ Scanned {config.SCAN_BATCH_SIZE} keys, no balance found")
        
        # Reset error counter on success
        error_count = 0
        
    except Exception as e:
        error_count += 1
        logger.error(f"❌ Scan job failed: {e}")
        
        if error_count >= MAX_ERRORS:
            logger.critical(f"🛑 Too many errors ({error_count}), stopping scheduler")
            stop_scheduler()


def start_scheduler():
    """Start the automated scanning scheduler"""
    if not config.ENABLE_AUTO_SCAN:
        logger.info("⏸️  Automated scanning is disabled (ENABLE_AUTO_SCAN=false)")
        return
    
    if scheduler.running:
        logger.warning("⚠️  Scheduler is already running")
        return
    
    # Add scan job with interval trigger
    scheduler.add_job(
        scan_job,
        trigger=IntervalTrigger(minutes=config.SCAN_INTERVAL_MINUTES),
        id='bitcoin_scan',
        name='Bitcoin Key Scanner',
        max_instances=config.MAX_CONCURRENT_SCANS,
        replace_existing=True
    )
    
    scheduler.start()
    logger.info(f"🚀 Scheduler started - scanning every {config.SCAN_INTERVAL_MINUTES} minutes")
    logger.info(f"   Batch size: {config.SCAN_BATCH_SIZE} keys")
    logger.info(f"   Max concurrent jobs: {config.MAX_CONCURRENT_SCANS}")


def stop_scheduler():
    """Stop the scheduler gracefully"""
    if scheduler.running:
        scheduler.shutdown(wait=True)
        logger.info("🛑 Scheduler stopped")


def get_scheduler_status():
    """Get current scheduler status"""
    return {
        "running": scheduler.running,
        "enabled": config.ENABLE_AUTO_SCAN,
        "interval_minutes": config.SCAN_INTERVAL_MINUTES,
        "batch_size": config.SCAN_BATCH_SIZE,
        "jobs": [
            {
                "id": job.id,
                "name": job.name,
                "next_run": str(job.next_run_time) if job.next_run_time else None
            }
            for job in scheduler.get_jobs()
        ]
    }
