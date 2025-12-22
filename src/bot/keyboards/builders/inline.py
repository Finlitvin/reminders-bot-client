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

    def buttons(self, texts: list[str], callback_prefix: str):
        row = [
            {"text": t, "callback_data": f"{callback_prefix}_{i}"}
            for i, t in enumerate(texts)
        ]
        self._rows.append(row)
        return self

    def build(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(self._rows)
