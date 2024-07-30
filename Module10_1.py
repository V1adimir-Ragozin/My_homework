from threading import Thread
from time import sleep
import datetime

now = datetime.datetime.now


start = now()

def write_words(word_count, file_name):
    file = open(file_name, "w+")
    for i in range(1, word_count+1):
        file.write("Какое-то слово N {}\n".format(i))
        sleep(0.1)
    print("Завершилась запись в файл {}".format(file_name))
    file.close()

def run_threads(thrds):
    start = now()
    for thr in thrds:
        thr.start()
        thr.join()
    elapsed = now() - start
    print("Работа потоков {}".format(elapsed))

t1 = Thread(target=write_words, args=(10, 'example1.txt'))
t2 = Thread(target=write_words, args=(30, 'example2.txt'))
t3 = Thread(target=write_words, args=(200, 'example3.txt'))
t4 = Thread(target=write_words, args=(100, 'example4.txt'))
t = [t1, t2, t3, t4]


t5 = Thread(target=write_words, args=(10, 'example5.txt'))
t6 = Thread(target=write_words, args=(30, 'example6.txt'))
t7 = Thread(target=write_words, args=(200, 'example7.txt'))
t8 = Thread(target=write_words, args=(100, 'example8.txt'))
t2 = [t5, t6, t7, t8]


if __name__ == "__main__":
    run_threads(t)
    run_threads(t2)