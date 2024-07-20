import os
import time


# for i in os.walk('.'):
#     print(i)

# filetime = os.path.getmtime(file[0])
# formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
# print(formatted_time)
#
# print('Текущая директория:', os.getcwd())
# print('Путь до неё:', os.path.join())
# file = [f for f in os.listdir() if os.path.isfile(f)]
# print(file)
#
# print(os.path.dirname('homework2.py'))
# print(os.path.join('d:', 'homework2.py'))
# print(os.path.dirname(r'D:\Учеба\Urban\Project\UrbanHomework\homework2.py'))




for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = (os.path.dirname(r'D:\Учеба\Urban\Project\UrbanHomework\homework2.py'))
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
          f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
