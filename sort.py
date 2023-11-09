from num2words import num2words
import itertools

N = int(input("Введите количество сотрудников: "))
distances = list(map(int, input("Введите расстояния от работы до домов сотрудников (через пробел): ").split()))
tariffs = list(map(int, input("Введите тарифы за проезд одного километра в такси (через пробел): ").split()))

min_cost = float('inf')
min_taxi = []


for permutation in itertools.permutations(range(N)):
    total_cost = 0
    taxi_arrangement = []

    for i in range(N):
        taxi = permutation[i]
        cost = distances[i] * tariffs[taxi]
        total_cost += cost
        
        taxi_arrangement.append(taxi + 1)


    if total_cost < min_cost:
        min_cost = total_cost
        min_taxi = taxi_arrangement


def convert_number_to_words(amount):
    if amount < 1 or amount > 100000:
        return "Сумма должна быть от 1 до 100 000"

    words = num2words(amount, lang='ru')

    last_digit = amount % 10
    if last_digit == 1 and amount % 100 != 11:
        currency = "рубль"
    elif 2 <= last_digit <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        currency = "рубля"
    else:
        currency = "рублей"

    result = words.capitalize() + " " + currency

    return result

result = convert_number_to_words(min_cost)