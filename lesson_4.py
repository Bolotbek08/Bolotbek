data_tuple = ('а', 6.13, 'К', 'а', 'О', True, 'м', 'р', 3, 'ш', 1, 'г')

# Создать два пустых списка letters и numbers

letters, numbers = [], []

# Пройтись циклом for по кортежу data_tuple, добавить все строки в список letters, а всё остальное в numbers.

for i in data_tuple:

   letters.append(i) if type(i) == str else numbers.append(i)

# реверсировать letters и изменить пару букв в letters.

letters = [str(i) for i in letters[::-1]]

letters[0], letters[1], letters[3], letters[4], letters[5], letters[6] = 'Г', 'а', 'М', 'о', 'ш', 'к'

# Из списка numbers удалить число 6.13 и переместить True в конец списка letters, затем вставить число 2 между 3 и 1

del numbers[0]

letters.append(numbers.pop(0))

numbers.insert(1, 2)

# Отсортировать numbers

numbers = [int(i) for i in numbers[::-1]]

# Измените список numbers в список квадратов своих же чисел

numbers = [int(i) ** 2 for i in numbers]

# Преобразовать списки numbers и letters в кортежи

letters = tuple(letters)

numbers = tuple(numbers)

# итог

print(letters)

print(numbers)