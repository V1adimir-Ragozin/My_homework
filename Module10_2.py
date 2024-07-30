from threading import Thread
from time import sleep
import datetime

now = datetime.datetime.now
start = now()


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100

    def run(self):
        print("{}, на нас напали!".format(self.name))
        day = 1
        self.enemy -= self.power
        while self.enemy > 0:
            print("{}, сражается {} день(дня)..., осталось {} воинов.".format(self.name, day, self.enemy))
            self.enemy -= self.power
            day += 1
            sleep(1)
        print("{} одержал победу спустя {} дней(дня)!".format(self.name, day))


end = now() - start
k = Knight('Sir Lancelot', 10)
k2 = Knight("Sir Galahad", 20)
knights = [k, k2]

for ks in knights:
    ks.start()
for ks in knights:
    ks.join()

print("Все битвы закончились!")