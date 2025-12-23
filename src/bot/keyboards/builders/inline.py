from telegram import InlineKeyboardMarkup

from bot.keyboards.builders.abc import KeyboardBuilder


class InlineKeyboardBuilder(KeyboardBuilder):
    def __init__(self):
        self._rows = []

    def button(self, text: str, callback_data: str, **kwargs):
        self._rows.append(
            [{"text": text, "callback_data": callback_data, **kwargs}]
        )
        return self

    def buttons(self, data: list[dict]):
        row = [
            {"text": t.get("text"), "callback_data": t.get("callback_data")}
            for t in data
        ]

        self._rows.append(row)
        return self

    def build(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(self._rows)
