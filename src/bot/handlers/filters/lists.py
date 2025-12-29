from telegram.ext import filters

from bot.constants.buttons import Buttons


class ShowListFilter(filters.MessageFilter):
    def __init__(self):
        self.name = "filters.ShowList"

    def filter(self, message):
        return message.text == Buttons.LISTS.value


SHOW_LIST_FILTER = ShowListFilter()
