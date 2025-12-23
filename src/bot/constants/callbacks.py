import re
from enum import Enum


class CallbackData(str, Enum):
    SPLIT_SYMBOL = "$"

    BACK = "back"
    REMINDER_LIST_ID = "reminder_list${id}"
    SECTION_ID = "section${id}"
    REMINDER_ID = "reminder${id}"


    @classmethod
    def reminder_list_id(cls, reminder_id: int) -> str:
        return cls.REMINDER_LIST_ID.value.format(id=reminder_id)

    @classmethod
    def section_id(cls, section_id: int) -> str:
        return cls.SECTION_ID.value.format(id=section_id)

    @classmethod
    def reminder_id(cls, reminder_id: int) -> str:
        return cls.REMINDER_ID.value.format(id=reminder_id)


PATTERNS = {
    "reminder_list": re.compile(r"^reminder_list\$(\d+)$"),
    "section": re.compile(r"^section\$(\d+)$"),
    "reminder": re.compile(r"^reminder\$(\d+)$"),
}
