from loguru import logger
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.clients import KWork
from app.core.config import settings, BASE_DIR, PARS_URLS
from app.schemas import Task


def get_tasks(url: str) -> list[Task]:
    logger.info(f"Получение задач по ссылке: {url}")
    response = KWork.get_response(url)
    text = response.text
    kwork = KWork(text)
    tasks = kwork.get_tasks()
    logger.info(f"Получено: {len(tasks)} задач")
    return tasks


@logger.catch
def main():
    sent_tasks_ids = []
    logger.info("Запуск")
    logger.info(f"Отслеживаемые ссылки: {PARS_URLS}")

    bot = TeleBot(settings.TELEGRAM_TOKEN, parse_mode="HTML")

    for url in PARS_URLS:
        tasks = get_tasks(url)

        for task in tasks:
            if task.id in sent_tasks_ids:
                continue

            keyboard = InlineKeyboardMarkup()
            keyboard.add(InlineKeyboardButton(text=str(task.price), url=task.url))
            bot.send_message(settings.USER_ID, task.text_for_tg, reply_markup=keyboard)
            sent_tasks_ids.append(task.id)
            break


if __name__ == "__main__":
    logger.add(BASE_DIR / 'logs' / "{time}.log")
    main()
