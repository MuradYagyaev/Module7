# Модуль №7. Работа с файлами и форматированный вывод. Режимы открытия файлов.

file_name = 'file_read.txt'
with open(file_name, mode='r',  encoding='utf8') as file:
    for line in file:
        print(line, end='')
