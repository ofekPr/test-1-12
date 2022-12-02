class employee:
    def __init__(self, name, id_num, salary):
        self.name = name
        self.id_num = id_num
        self.salary = salary

    def set_salary(self, salary):
        self.salary = salary

    def __str__(self):
        return f"{self.name=} {self.salary=} {self.id_num=}"


class manager(employee):
    def __init__(self, name, id_num, salary, yearly_bonus):
        self.name = name
        self.id_num = id_num
        self.salary = salary
        self.yearly_bonus = yearly_bonus

    def __str__(self):
        return f"{self.name=} {self.salary=} {self.id_num=} {self.yearly_bonus=}"


e1 = employee("e1", '000000000', 12340)
e2 = employee("e2", '000000001', 13456)
m1 = manager("m1", '000000002', 123456, 123)

print(e1)
print(e2)
print(m1)


