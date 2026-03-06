from telegram import Update
from telegram.ext import ContextTypes
from bot.database.models import add_new_task, get_all_tasks
from bot.utils.helpers import parse_date

async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Пример: /add_task Реферат по истории, 6 марта 2026
        args = context.args
        if len(args) < 2:
            await update.message.reply_text("Ошибка: Укажите название задачи и дату.")
            return

        title = args[0]
        due_date_str = " ".join(args[1:])
        due_date = parse_date(due_date_str)  # Парсинг даты из "6 марта 2026" или "завтра"

        if not due_date:
            await update.message.reply_text("Ошибка: Неверный формат даты.")
            return

        # Сохранение задачи
        add_new_task(update.effective_user.id, title, due_date)
        await update.message.reply_text(f"Задача '{title}' добавлена. Напомним за день до срока.")

    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")

async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tasks = get_all_tasks(update.effective_user.id)
    if not tasks:
        await update.message.reply_text("У вас нет активных задач.")
        return

    response = "\n".join([f"{i+1}. {task.title}. Срок: {task.due_date.strftime('%d %B %Y')}"
                         for i, task in enumerate(tasks)])
    await update.message.reply_text(response)
