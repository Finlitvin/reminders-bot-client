from telegram.ext import filters

from bot.constants.buttons import Buttons


class CreateReminderFilter(filters.MessageFilter):
    def __init__(self):
        self.name = "filters.CreateReminder"

    def filter(self, message):
        return message.text == Buttons.ADD.value


CREATE_REMINDER_FILTER = CreateReminderFilter()
