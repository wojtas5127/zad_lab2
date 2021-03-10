import sys as system
from math import *

#zad1

# lista = ["unihokej", "pilka reczna", "pilka nozna", "siatkowka"]
#
# lista.reverse()
# print(lista)

#zad2

# slownik = {"wyd": "wydanie", "tlum": "tłumaczenie", "jw": "jak wyżej", "por": "odesłanie do innych prac"}
#
# print(slownik)

#zad3

# slownik = {1: "League of legends", 2: "wiedźmin 3", 3: "GTA V", 4: "Counter strike", 5: "Shakes and fidget"}
#
# d = len(slownik.keys())
#
# print("W słowniku jest %d elementów" % (d))

#zad4

# zdanie = input("Podaj zdanie ")
#
# c = zdanie.count("a")
#
# print("Zdanie ma %d litery a" % (c))

#zad5

# system.stdout.write("wpisz liczby: ")
# a = system.stdin.readline()
# b = system.stdin.readline()
# c = system.stdin.readline()

# liczba = pow(int(a), int(b)) + int(c)
#
# system.stdout.write(str(liczba))

#zad6

# a = input("wpisz pierwszą liczbe ")
# b = input("wpisz drugą liczbe ")
# c = input("wpisz trzecią liczbe ")
#
# a = int(a)
# b = int(b)
# c = int(c)
#
# if b>a:
#     if b>c:
#         print("b jest najwieksze")
#     else:
#         print("c jest najwieksze")
# else:
#     print("a jest największe")

#zad7

# lista = [3, 45, 4.56, 7.5, 6.9, 4.20]
#
# for x in lista:
#     k = pow(x,2)
#     print(k)

#zad8

# l = []
# n = 0
# while n < 10:
#     number = int(input("Podaj liczbe "))
#     if number % 2 == 0:
#         l.append(number)
#     n += 1
# print(l)

#zad9

# lista = [1,2,3,4,5]
#
# for i in lista:
#     if i % 2 == 0:
#         print("E")
#     else:
#       print("EEEEEE")

#zad10

# liczba = input("Podaj liczbę: ")
#
# liczba = int(liczba)
#
# if liczba<0:
#     print("Liczba nie może być ujemna")
# else:
#     d = sqrt(liczba)
#     print(d)