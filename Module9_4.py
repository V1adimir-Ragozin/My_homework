first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)


def get_advanced_wrinter(file_name):
    def write_everything(*data_set):
        with open('Module9_4.txt', 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(str(data) + '\n')

    return write_everything


write = get_advanced_wrinter('Module9_4.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

import random


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
