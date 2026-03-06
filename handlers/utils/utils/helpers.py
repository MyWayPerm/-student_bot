from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot.database.models import get_tasks_for_reminder
from bot.config import REMINDER_TIME

def setup_scheduler(app):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        check_reminders,
        "cron",
        hour=REMINDER_TIME.hour,
        minute=REMINDER_TIME.minute,
        args=[app],
    )
    scheduler.start()

async def check_reminders(app):
    tasks = get_tasks_for_reminder()
    for task in tasks:
        await app.bot.send_message(
            task.user_id,
            f"Напоминание! Сегодня срок сдачи задачи: {task.title}."
        )
