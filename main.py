## Task - 6

## Problem 1: Bank Account Management System

class BankAccount:

    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self._balance = initial_balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        # Adds money to the balance if the amount is valid.
        if amount > 0:
            self._balance = self._balance + amount

    def withdraw(self, amount):
        # Withdraws money if there are enough funds.
        if amount > 0 and self._balance >= amount:
            self._balance = self._balance - amount
            return True
        return False


class SavingsAccount(BankAccount):
    # Savings account that calculates interest over the balance.

    def __init__(self, account_number, initial_balance, interest_rate):
        BankAccount.__init__(self, account_number, initial_balance)
        self.interest_rate = interest_rate  # Example: 0.05 for 5%

    def calculate_interest(self):
        # Calculates interest based on the current balance.
        current_balance = self.get_balance()
        interest_amount = current_balance * self.interest_rate
        return interest_amount


class CurrentAccount(BankAccount):

    def __init__(self, account_number, initial_balance, min_balance):
        BankAccount.__init__(self, account_number, initial_balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        # Overriding withdraw to ensure balance stays above minimum limit.
        current_balance = self.get_balance()
        if amount > 0 and (current_balance - amount) >= self.min_balance:
            self._balance = self._balance - amount
            return True
        return False


if __name__ == "__main__":
    print("--- Problem 1: Bank Accounts ---")

    # Test SavingsAccount
    my_savings = SavingsAccount("SAV99", 1000.0, 0.05)
    interest = my_savings.calculate_interest()
    print("Savings Account Interest Amount:", interest)

    # Test CurrentAccount
    my_current = CurrentAccount("CUR11", 500.0, 200.0)

    # Trying to withdraw 400 would drop balance to 100 (violates min_balance of 200)
    did_withdraw = my_current.withdraw(400.0)
    print("Is withdrawal of $400 successful?:", did_withdraw)
    print("Current Account Balance:", my_current.get_balance())

print("===================================================================")

# Problem 2: Employee Management System
# This module calculates salaries using inheritance and polymorphism structures.

class Employee:
    # A base class representing a generic employee.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        # Base calculation method.
        return self.salary


class RegularEmployee(Employee):
    # A permanent employee who receives a salary plus an allowance.
    def __init__(self, name, salary, allowance):
        Employee.__init__(self, name, salary)
        self.allowance = allowance

    def calculate_salary(self):
        # Adds monthly allowance to base salary.
        return self.salary + self.allowance


class ContractEmployee(Employee):
    # An employee paid entirely by hourly rates.
    def __init__(self, name, hourly_rate, hours_worked):
        # Contract employees start with a base monthly salary configuration of 0
        Employee.__init__(self, name, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        # Calculates earnings based on time logged.
        return self.hourly_rate * self.hours_worked

class Manager(Employee):
    # A manager who receives a salary plus a performance bonus.
    def __init__(self, name, salary, performance_bonus):
        Employee.__init__(self, name, salary)
        self.performance_bonus = performance_bonus

    def calculate_salary(self):
        # Adds performance bonus to base salary.
        return self.salary + self.performance_bonus


if __name__ == "__main__":
    print("--- Problem 2: Employee Management ---")

    emp1 = RegularEmployee("Alice", 3000, 500)
    emp2 = ContractEmployee("Bob", 40, 80)
    emp3 = Manager("Charlie", 6000, 1500)

    # Polymorphism: Iterating over the list and calling the same method name
    employee_list = [emp1, emp2, emp3]
    for employee in employee_list:
        print(f"Employee: {employee.name} | Total Salary: {employee.calculate_salary()}")

print("===================================================================")

# Problem 3: Vehicle Rental System

class Vehicle:
    # A base class representing a generic rental vehicle.
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        # Base calculation formula for rental duration.
        return self.rental_rate * days


class Car(Vehicle):
    # A standard car rental that adds a flat cleaning/service fee.
    def __init__(self, model, rental_rate, service_fee=15.0):
        Vehicle.__init__(self, model, rental_rate)
        self.service_fee = service_fee

    def calculate_rental(self, days):
        # Computes rate by adding standard flat service charges.
        base_cost = self.rental_rate * days
        total_cost = base_cost + self.service_fee
        return total_cost

class Bike(Vehicle):
    # A motorcycle rental that gives a small discount based on day count.
    def __init__(self, model, rental_rate, discount_per_day=2.0):
        Vehicle.__init__(self, model, rental_rate)
        self.discount_per_day = discount_per_day

    def calculate_rental(self, days):
        # Applies a multi-day discount calculation.
        total_cost = (self.rental_rate * days) - (self.discount_per_day * days)
        return total_cost

class Truck(Vehicle):
    # A heavy truck rental that factors in cargo weight capacity.
    def __init__(self, model, rental_rate, cargo_weight):
        Vehicle.__init__(self, model, rental_rate)
        self.cargo_weight = cargo_weight  # weight measured in tons

    def calculate_rental(self, days):
        # Applies extra flat rate per ton capacity.
        weight_surcharge = 50.0 * self.cargo_weight
        total_cost = (self.rental_rate * days) + weight_surcharge
        return total_cost

if __name__ == "__main__":
    print("--- Problem 3: Vehicle Rental System ---")

    car1 = Car("Sedan", 40.0)
    bike1 = Bike("Cruiser", 20.0)
    truck1 = Truck("Cargo Van", 100.0, 2.5)

    rental_days = 5
    vehicle_list = [car1, bike1, truck1]

    # Polymorphism: Running the unique calculations using a simple loop
    for vehicle in vehicle_list:
        cost = vehicle.calculate_rental(rental_days)
        print(f"Vehicle: {vehicle.model} | Cost for {rental_days} days: {cost}")

print("===================================================================")