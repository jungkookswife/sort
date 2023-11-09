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