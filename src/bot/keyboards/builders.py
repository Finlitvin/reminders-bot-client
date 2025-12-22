from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class KeyboardBuilder:
    def __init__(self):
        self.reset()

    @property
    def keyborad(self) -> InlineKeyboardMarkup:
        self.next_row()
        keybord = self._keyboard
        self.reset()
        return InlineKeyboardMarkup(keybord)

    def reset(self) -> None:
        self._buttons = []
        self._keyboard = []

    def add_button(self, text: str, callback_data: str):
        self._buttons.append(
            InlineKeyboardButton(text, callback_data=callback_data)
        )

    def next_row(self) -> None:
        if self._buttons:
            self._keyboard.append(self._buttons)
            self._buttons = []
