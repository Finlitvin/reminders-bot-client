from re import Pattern
from enum import Enum


class Callbacks(str, Enum):
    BACK = "back"
    LIST_SELECT = "list_select${id}"
    CATEGORY_SELECT = "category_select${id}"
    REMINDER_SELECT = "reminder_select${id}"
    REMINDER_DONE = "reminder_done${id}"
    REMINDER_DELETE = "reminder_delete${id}"
    REMINDER_EDIT = "reminder_edit${id}"

    @classmethod
    def list_select(cls, list_id: int) -> str:
        return cls.LIST_SELECT.value.format(id=list_id)

    @classmethod
    def category_select(cls, category_id: int) -> str:
        return cls.CATEGORY_SELECT.value.format(id=category_id)

    @classmethod
    def reminder_select(cls, reminder_id: int) -> str:
        return cls.REMINDER_SELECT.value.format(id=reminder_id)

    @classmethod
    def reminder_done(cls, reminder_id: int) -> str:
        return cls.REMINDER_DONE.value.format(id=reminder_id)

    @classmethod
    def reminder_delete(cls, reminder_id: int) -> str:
        return cls.REMINDER_DELETE.value.format(id=reminder_id)

    @classmethod
    def reminder_edit(cls, reminder_id: int) -> str:
        return cls.REMINDER_EDIT.value.format(id=reminder_id)

    @property
    def pattern(self) -> Pattern[str]:
        return f"^{self.value.split('$')[0]}"
