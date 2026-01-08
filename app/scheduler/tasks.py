from apscheduler.schedulers.background import BackgroundScheduler
from app.config import settings
import logging

logger = logging.getLogger(__name__)
_scheduler = None

def start_scheduler():
    """Start background scheduler."""
    global _scheduler
    _scheduler = BackgroundScheduler(timezone=settings.timezone)
    
    # TODO: Add job
    # _scheduler.add_job(
    #     daily_analysis_job,
    #     trigger="cron",
    #     hour=settings.analysis_hour,
    #     minute=settings.analysis_minute,
    #     id="daily_analysis",
    # )
    
    _scheduler.start()
    logger.info(f"✅ Scheduler started. Analysis: {settings.analysis_hour}:{settings.analysis_minute:02d} CET")

def stop_scheduler():
    """Stop scheduler."""
    global _scheduler
    if _scheduler:
        _scheduler.shutdown()
        logger.info("🛑 Scheduler stopped.")

async def daily_analysis_job():
    """Daily analysis task."""
    logger.info("▶️ Starting daily analysis job...")
    # TODO: Implement
    logger.info("✅ Daily analysis job completed.")
