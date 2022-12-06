import random

# print("Test")

# x = 1
# if x < 10:
#     print("x < 10")
# elif x == 10:
#     print("x = 10")
# elif x == 1:
#     print("x = 1")
# else:
#     print("Inna wartosc")

# words = ['kot', 'okno', 'rower']
# # print(words)


# for nazwa_zmiennej in words:
#     print(nazwa_zmiennej)

# print(nazwa_zmiennej)

# number = [0,1,2,3,4]
# name = " Bartosz"
# number = list(range(5))

# for i in range(100, 110, 5):
#     print(str(i) + name)


# for i in range(0,100):
#     division = i % 2

#     if division == 0:
#         print(str(i) + " - Parzysta")
#     elif division == 1:
#         print(str(i) + " - Nieparzysta")

# for i in range(0,100):
#     if i > 50:
#         break

#     division = i % 2

#     if division == 0:
#         print(str(i) + " - Parzysta")
#         continue 
    
#     print(str(i) + " - Nieparzysta")

#     print("Koniec petli")

# is_run = True
# index = 0

# while is_run:
#     print(str(index))
#     if index >= 10:
#         is_run = False
#     index = index + 1



# index = 0
# while True:
#     print(str(index))
#     if index >= 10:
#         break
#     index = index + 1


# numbers = [12,124,43,6,4,34,2,123,12,31]
# chars = ['a', 'c', 'z', 'y' , 'i', 'ab', 'aa', 'aba']
# print("Min:" + str(min(numbers)))
# print("Max:" + str(max(numbers)))

# print("Min:" + str(min(chars)))
# print("Max:" + str(max(chars)))

# # print(min(list([])))

# print(ord('Z'))

# x = 1
# if x < 10:
#     print("x < 10")
# elif x == 10:
#     print("x = 10")
# elif x == 1:
#     print("x = 1")
# else:
#     print("Inna wartosc")


# x = 1
# match x :
#     case 10:
#         print("x = 10")
#     case 1:
#         print("x = 1")
#     case default:
#         print("Inna wartosc")


for i in range(100):
    print(random.randint(0, 1000))
