import random


def format_welcome_message(username: str) -> str:
    greetings = [
        f"👋 Привет, {username}!",
        f"✨ Добро пожаловать, {username}!",
        f"🚀 Рад видеть, {username}!",
        f"🌟 Здравствуй, {username}!",
    ]

    greeting = random.choice(greetings)

    return (
        f"{greeting}\n\n"
        f"🤖 *Я бот для управления напоминаниями*\n\n"
        f"Я помогу вам:\n"
        f"• ⏰ Создавать напоминания\n"
        f"• 🔄 Настраивать повторения\n"
        f"• 📅 Планировать задачи\n"
        f"• 🔔 Получать уведомления\n\n"
        f"Используйте кнопки ниже для навигации 📱"
    )
