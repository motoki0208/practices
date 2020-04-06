from abc import ABCMeta

from consts import CallLevel


class OperatorBase(metaclass=ABCMeta):
    DISPLAY_CLASS_NAME = None
    DEALABLE_LEVEL = None

    def __init__(self, name):
        self.name = name
        self.is_free = True
        self.next = None

    @property
    def name_with_class(self):
        return f"{self.__class__.DISPLAY_CLASS_NAME}/{self.name}"

    def set_next(self, senior_operator):
        self.next = senior_operator

    def can_deal(self, call) -> bool:
        if self.is_free and self.__class__.DEALABLE_LEVEL >= call.level:
            return True

        return False

    def deal(self, call):
        print(f"{self.name_with_class}が{call}の受付をします")
        self.is_free = False

class Operator(OperatorBase):
    DISPLAY_CLASS_NAME = "応答者"
    DEALABLE_LEVEL = CallLevel.EASY


class Manager(OperatorBase):
    DISPLAY_CLASS_NAME = "マネージャー"
    DEALABLE_LEVEL = CallLevel.NORMAL


class Director(OperatorBase):
    DISPLAY_CLASS_NAME = "ディレクター"
    DEALABLE_LEVEL = CallLevel.DIFFICULT
