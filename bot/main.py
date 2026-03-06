import logging
from telegram.ext import Application, CommandHandler
from bot.handlers.tasks import add_task, list_tasks
from bot.utils.helpers import setup_scheduler
from bot.database.models import init_db
from bot.config import TELEGRAM_TOKEN

# Настройка логирования
logging.basicConfig(level=logging.INFO)

def main():
    # Инициализация базы данных
    init_db()

    # Создание бота
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Обработчики команд
    app.add_handler(CommandHandler("add_task", add_task))
    app.add_handler(CommandHandler("tasks", list_tasks))

    # Запуск планировщика для напоминаний
    setup_scheduler(app)

    # Запуск бота
    app.run_polling()

if __name__ == "__main__":
    main()
