from bot.keyboards.builders import ReplyKeyboardBuilder


def get_main_menu():
    return (
        ReplyKeyboardBuilder()
        .resize()
        .button("📋 Список напоминаний")
        .button("⚙️ Настройки")
        .build()
    )
