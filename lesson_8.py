# w - режим записи, перезаписи
# a - режим записи, дозаписи
# x - режим бесконфликтного записи файла

file = open('file.txt', 'w', encoding='UTF-8')
file.write('Бишкек, Кыргызстан')
file.close()

with open('file.txt', 'a', encoding='UTF-8') as file:
    file.write('новая строка')

with open('file.txt', 'x', encoding='UTF-8') as file:
    file.write('новая строка')

with open('file.txt', 'r', encoding='UTF-8') as file:
    print(file.read())