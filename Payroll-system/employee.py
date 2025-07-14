

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

class Hourly_Employee(Employee):
    def __init__(self, name, emp_id, salary, hours_worked, hourly_rate):
        super().__init__(name, emp_id, salary)  
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate    
   

class Salaried_Employee(Employee):
    def __init__(self, name, emp_id, salary,monthly_salary):
        super().__init__(name, emp_id, salary)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        total_salary=super().calculate_salary.self
        return self.monthly_salary

class CommissionEmployee(Salaried_Employee):
    def __init__(self, emp_id, name, weekly_salary, commission):
        super().__init__(emp_id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return self.weekly_salary + self.commission

