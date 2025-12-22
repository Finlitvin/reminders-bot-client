from bot.keyboards.builders import ReplyKeyboardBuilder


def get_main_menu():
    return (
        ReplyKeyboardBuilder()
        .resize()
        .buttons(["Список напоминаний", "Настройки"])
        .build()
    )
