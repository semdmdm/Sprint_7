class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email


    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is not None:
            hours = hours
        else:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)


    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is not None:
            email = email
        else:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)


    @classmethod
    def set_hourly_payment(cls, hourly_payment_new):
        cls.hourly_payment = hourly_payment_new


    def salary(self):
        return self.hours * self.hourly_payment

# Для отображения корректности работы, сформулировал сразу и запросы с данными и со значением "None".
# Где значения "None", корректной передачи в функции и переменные не получилось без использования созданного объекта employeesalary,
# т.к. salary не расчитывается из-за разных типов данных

employeesalary = EmployeeSalary.get_hours("Dmitriy", 36, 3, "big@mail.ru")
employeesalary = EmployeeSalary.get_email("Dmitriy", 36, 3, "big@mail.ru")

print(employeesalary.name)
print(employeesalary.hours)
print(employeesalary.rest_days)
print(employeesalary.email)
print(EmployeeSalary.hourly_payment)
print(employeesalary.salary())

EmployeeSalary.set_hourly_payment(700)

print(EmployeeSalary.hourly_payment)
print(employeesalary.salary())


employeesalary = EmployeeSalary.get_hours("Dmitriy", None, 4, None)
employeesalary = EmployeeSalary.get_email(employeesalary.name, employeesalary.hours, employeesalary.rest_days, employeesalary.email)

print(employeesalary.name)
print(employeesalary.hours)
print(employeesalary.rest_days)
print(employeesalary.email)
print(EmployeeSalary.hourly_payment)
print(employeesalary.salary())

EmployeeSalary.set_hourly_payment(900)

print(EmployeeSalary.hourly_payment)
print(employeesalary.salary())