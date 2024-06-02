# Модуль №7. Работа с файлами и форматированный вывод. Файлы в операционной системе.

import os
import time

directory = '.'

for dirpath, dirnames, filenames in os.walk(directory):
    for file in filenames:
        filepath = os.path.join(directory, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
            f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')