
# region подстановка
line = ("a", "b", "c")
line2 = dict(name="point1", size=(100, 200))

# print("{0}{1}{2}".format(*[1, 2, 5]))
# print("{name}{size}".format(**line2))
# endregion

#
# print("начало{a:6}.".format(a="start")) # дополнить до 10 символов
# print("начало{a:6}.".format(a="start")) # дополнить до 10 символов


##################################################

# region выровнять по правой стороне
# дополнить с левой стороны с левой стороны
# print("начало{a:>12}.".format(a="startxxxxx"))
# print("начало{a:>12}.".format(a="startxxx"))

# endregion


# region Description
# здесь одиноковые результаты
# print("начало{a:<12}.".format(a="startxxxxx"))
# print("начало{a:12}.".format(a="startxxxxx"))
# endregion




# region выровнять по центру
# дополнить с обоих сторон
# print("начало{a:^12}.".format(a="startxxxxx"))
# print("начало{a:^12}.".format(a="start"))
# endregion

# ЧИСЛА

# print("в двоичный - {:b}".format(2))
# print("дополнить нулями - {:05}".format(1))
print("{:+=8}".format(5))

# region получить атрибут

class Dog:
    def __init__(self, name):
        self._name = name

    def height(self):
        return 10

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return self.name

    def __str__(self):
        return "dog_name - {}".format(self.name)

muhtar = Dog("muhtar")
# получить атрибут
# print("{dog.name}".format(dog=muhtar))
# но не выполнить код
# print("{dog.height()}".format(dog=muhtar))
bob = Dog("bob")
print("{!s}".format(bob))
# endregion

# print("{n[1]}".format(n="abc"))
# так нельзя
# print("{n[-1]}".format(n="abc"))

serg = dict(name="serg", weight=56)
# print("{atr[name]}".format(atr=serg))
# print('{0}'.format(4/3))



