from typing import Any
from abc import ABC, abstractmethod


class KeyboardBuilder(ABC):
    """Общий интерфейс для всех клавиатурных билдеров"""

    @abstractmethod
    def button(self, text: str, **kwargs) -> "KeyboardBuilder":
        """Добавить одну кнопку"""
        pass

    @abstractmethod
    def buttons(self, texts: list[str], **kwargs) -> "KeyboardBuilder":
        """Добавить несколько кнопок в строку"""
        pass

    @abstractmethod
    def build(self) -> Any:
        """Построить клавиатуру"""
        pass
