from abc import ABCMeta, abstractmethod


class FinancialInstitution(metaclass=ABCMeta):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self._is_for_profit = True
        self._balance = 0
        self._is_atm_service = False
        self._is_retail_banking = True

    # Enforce implementation of parent method for subclasses that inherit this class,
    #  to separate the interface from implementation details.
    @abstractmethod
    def deposit_money(self, amount):
        self._balance += amount

    @abstractmethod
    def withdraw_money(self, amount):
        if self._balance - amount < 0:
            print("Your balance would go below zero (0) with a withdraw of ${0}!".format(amount))
            print("Current Balance: ${0}".format(self._balance))
        else:
            self._balance -= amount

    @abstractmethod
    def transfer_to_another_fi(self, fi, amount):
        self.withdraw_money(amount)
        self.show_balance
        # How to prevent overwithdrawing???
        fi.deposit_money(amount)

    @property # getter, not a method. Read-only property.
    @abstractmethod # must be the innermost decorator
    def show_balance(self):
        return self._balance


class Bank(FinancialInstitution):
    def __init__(self, name, address):
        super(Bank, self).__init__(name, address)
        self._is_atm_service = True

    def deposit_money(self, amount):
        super().deposit_money(amount)

    def withdraw_money(self, amount):
        super().withdraw_money(amount)

    def transfer_to_another_fi(self, fi, amount):
        super().transfer_to_another_fi(fi, amount)

    def show_balance(self):
        return self.show_balance()


class CreditUnion(FinancialInstitution):
    def __init__(self, name, address):
        super(CreditUnion, self).__init__(name, address)
        self._is_for_profit = False

    def deposit_money(self, amount):
        super().deposit_money(amount)

    def withdraw_money(self, amount):
        super().withdraw_money(amount)

    def transfer_to_another_fi(self, fi, amount):
        super().transfer_to_another_fi(fi, amount)

    def show_balance(self):
        return self.show_balance()




# class Insurance(FinancialInstitution):
#     def __init__(self, name, address):
#         super(Insurance, self).__init__(name, address)
#         self._is_retail_banking = False


bank_a = Bank("Bank A", "129 West 81st Street, Apartment 5A")
print("Name: " + bank_a.name + " " + "Address: " + bank_a.address)

bank_a.deposit_money(200)
print(bank_a.show_balance)
bank_a.withdraw_money(100)
bank_a.withdraw_money(200)

credit_b = CreditUnion("Credit Union B", "2707 Martin Luther King Jr Ave SE")
bank_a.transfer_to_another_fi(credit_b, 50)
print(credit_b.show_balance)
