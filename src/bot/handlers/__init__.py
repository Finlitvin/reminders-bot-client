from . import lists, categories, commands, reminders


def get_all_handlers() -> list:
    return (
        commands.get_handlers()
        + lists.get_handlers()
        + categories.get_handlers()
        + reminders.get_handlers()
    )
