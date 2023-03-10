# ten = list(range(1, 11))
# evens = list(filter(lambda n: n % 2 == 0, ten))
# print(evens)
# print(list(map(lambda x: x**2, evens)))
#
# def get_by_index(lst=ten):
#     while True:
#         try:
#             index_object = int(input('введите индекс: '))
#             print(lst[index_object])
#         except ValueError:
#             print('вводите только числа!')
#         except IndexError:
#             print("введите правильный индекс")
#         if index_object == 100:
#             print('Вы закончили операцию')
#             break
# get_by_index('python')
 # get_by_index()


import codewars_test as test
from solution import even_or_odd


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(even_or_odd(2), "Even")
        test.assert_equals(even_or_odd(1), "Odd")
        test.assert_equals(even_or_odd(0), "Even")
        test.assert_equals(even_or_odd(1545452), "Even")
        test.assert_equals(even_or_odd(7), "Odd")
        test.assert_equals(even_or_odd(78), "Even")
        test.assert_equals(even_or_odd(17), "Odd")
        test.assert_equals(even_or_odd(74156741), "Odd")
        test.assert_equals(even_or_odd(100000), "Even")
        test.assert_equals(even_or_odd(-123), "Odd")
        test.assert_equals(even_or_odd(-456), "Even")


@test.describe("Random Tests")
def random_tests():
    from random import randint

    def sol(n):
        return ["Even", "Odd"][n % 2]

    for _ in range(100):
        num = randint(-1e4, 1e7)

        @test.it(f"Testing for even_or_odd({num})")
        def test_case():
            test.assert_equals(sol(num), even_or_odd(num), "It should work for random inputs too")