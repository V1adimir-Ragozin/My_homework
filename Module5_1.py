class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int) -> None:
        if self.number_of_floors < new_floor:
            print("Такого этажа не существует")
            return # завершение функции и вывод результата выполнения функции. В данном случае ничего.
        for i in range(1, new_floor + 1):
           print(i)



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)