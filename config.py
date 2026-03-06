from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///tasks.db")
REMINDER_TIME = datetime.strptime(os.getenv("REMINDER_TIME", "09:00"), "%H:%M").time()
