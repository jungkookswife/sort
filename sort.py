from num2words import num2words
import itertools

N = int(input("Введите количество сотрудников: "))
distances = list(map(int, input("Введите расстояния от работы до домов сотрудников (через пробел): ").split()))
tariffs = list(map(int, input("Введите тарифы за проезд одного километра в такси (через пробел): ").split()))