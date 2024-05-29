# Модуль №7. Работа с файлами и форматированный вывод. Режимы открытия файлов.

file_name = 'file_read.txt'
file = open(file_name, mode='r')
file_content = file.read()
print(file_content)
file.close()
