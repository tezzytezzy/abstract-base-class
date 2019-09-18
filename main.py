from abc import ABCMeta, abstractmethod

class Financial_Institution(metaclass=ABCMeta):
    def __init__(self, name, address):
        pass

class Bank(Financial_Institution):
    def __init__(self):
        super().__init__()
        self._is_online_only = False

    def deposit_money(self, amount):
        pass

    def withdraw_money(self, amount):
        pass

    def transfer_to_another_fi(self, amount):
        pass




