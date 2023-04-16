class My_Exceptions:
    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if type(value) is str:
            instance.__dict__[self.my_attr] = value
        else:
            raise ValueError("Вы ввели цифры")

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker():
    name = My_Exceptions()
    surname = My_Exceptions()

    def __init__(self, name, surname, salary, bonus):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.bonus = bonus

    def wage_work(self):
        print(f"Ваше имя - {self.name}, Ваша фамилия - {self.surname}")
        wage = self.salary + self.bonus
        return wage


obj = Worker('Kirill', 2, 100, 50)
print(obj.wage_work())
