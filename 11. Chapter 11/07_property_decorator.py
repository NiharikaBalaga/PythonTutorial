class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    #totalSalary = 6000

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val


e = Employee()
# print(e.totalSalary)
e.totalSalary = 800
print(e.totalSalary)
# print(e.salary)
print(e.salarybonus)
