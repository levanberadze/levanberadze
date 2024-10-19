from datetime import date


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    @property
    def budget(self):
        return sum(customer.balance for customer in self.customers)

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer):
        if customer in self.customers:
            self.customers.remove(customer)
        else:
            print("customer not found")

    def can_get_loan(self, customer, amount):
        return customer.balance >= amount * 0.5


class Customer:
    def __init__(self, name, date_of_birth: date, balance):
        self.name = name
        self.date_of_birth = date_of_birth
        self.balance = balance

    @property
    def age(self):
        return date.today().year - self.date_of_birth.year

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("you don`t have enough money")


if __name__ == "__main__":
    bank = Bank("bank")

    customer = Customer(
        name="Levan Beradze",
        date_of_birth=date(2008, 12, 17),
        balance=1700.0
    )

    bank.add_customer(customer)

    print(f"Name: {customer.name}")
    print(f"Age: {customer.age}")
    print(f"Balance: {customer.balance}")

    customer.deposit(300.0)
    print(f"Balance updated: {customer.balance}")

    customer.withdraw(500.0)
    print(f"balance updated: {customer.balance}")

    loan_amount = 1500.0
    if bank.can_get_loan(customer, loan_amount):
        print("Successful")
    else:
        print("Failed")