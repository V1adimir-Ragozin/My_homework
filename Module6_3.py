class Horse:  # класс описывающий лошадь.
    x_distance = 0  # атрибут класса, Пройденный путь
    sound = 'Frrr'  # атрибут класса, Звук, который издает лошадь

    def __init__(self):  # инициализатор, непонятно чего
        self.sound = super().sound

    def run(self, dx):  # метод, Изменение дистанции, увеличивает x_distance на dx
        self.x_distance += dx


class Eagle:  # класс описывающий орла.
    y_distance = 0  # атрибут класса, Высота полёта
    sound = 'I train, eat, sleep, and repeat'  # атрибут класса, Звук, который издает орёл

    def fly(self, dy):  # метод, Изменение дистанции, увеличивает y_distance на dy
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
