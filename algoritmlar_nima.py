'''01/10/2025'''

# >>>---------------------------->># 01 ALGORITM NIMA <<-----------------------------<<< #


# m1

''' Foydalanuvchi kiritgan ikki  sonni qo'shish algoritmi '''

# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))

# summa = num1 + num2
# print(f"Natija: {summa}")


# m2

''' Uchta sondan eng kattasini topish algoritmi '''

# a = int(input("a= "))
# b = int(input("b= "))
# c = int(input("c= "))

# if a > b and a > c:
#     print(f"Max num: {a}")
# elif b > a and b > c:
#     print(f"Max num: {b}")
# else:
#     print(f"Max son: {c}")




# m3


''' N faktorialni hisoblash algoritmi '''

# n = int(input("n= "))
# factorial= 1
# for i in range(1, n+1):
#     factorial *= i
# print(f"{i} Factorial= {factorial}")



# >>>------------------------------->> AMALIYOT <<-------------------------------<<< #


# M1 # >>>----------->> 🟢 Sodda masalalar

''' 1.Uchburchak perimetrini hisoblash '''

# a = int(input("a= "))
# b = int(input("b= "))
# c = int(input("c= "))

# if a and b and c != 0:
#     if a + b > c and a + c > b and b + c > c:
#         P = a + b + c
#         print(f"Uchburchak yuzasi: {P}")
#     elif a + c == b and a + b == c and a + c == b:
#         P = a + b + c
#         print(f"Uchburchak yuzasi: {P}") 
#     else:
#         print(f"{a, b, c} qiymatlar orqali uchburchak yasab bolmaydi! ")

# else:
#     print("Uchburchakning hechqachon bir tamoni 0 teng bolmaydi ")




# M2 

''' Son juft yoki toqligini aniqlash '''

# a = int(input("a= "))
# if a % 2 == 0:
#     print(f"Juft son: {a}")
# else:
#     print(f"Toq son: {a}")



# M3  

''' To‘rtburchak yuzasini hisoblash '''

# a = int(input("a= "))
# b = int(input("b= "))
# S = a * b
# print(f"Tortburchak yuzi: {S}")



# >>>---------------->>🟡 O‘rta:

# M4
''' 1 dan N gacha bo‘lgan sonlar yig‘indisi '''

# n= int(input("n= "))
# summa = 0
# for i in range(1, n+1):
#     summa += i
# print(f"Yig'indi: {summa}")


# M5
''' Uchta sondan eng kichigi '''

# a= int(input("a= "))
# b= int(input("b= "))
# c= int(input("c= "))

# if a < b and a < c:
#     print(f"Min: {a}")
# elif b < a and b <c:
#     print(f"Min: {b}")
# else:
#     print(f"Min: {c}")



# M6
''' Sonning bo‘luvchilari '''

# a= int(input("a= "))

# for i in range(1, a+1):
#     if a % i == 0:
#         print(i)




# >>>---------------->> 🔴 Yuqori:

# M7

# n= int(input("a= "))
# a, b = 0, 1
# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c



# M8

"""# Tub son tekshirish"""
# import math

# n = int(input("Sonni kiriting: "))

# if n < 2:
#     print("Tub emas")
# else:
#     tub = True
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             tub = False
#             break
#     if tub:
#         print("Tub son")
#     else:
#         print("Tub emas")




# M9

"""# Matndagi unlilar soni"""

# matn = input("Matn kiriting: ")
# unlilar = "aeiouAEIOUo‘u‘O‘U‘"
# count = 0

# for belgi in matn:
#     if belgi in unlilar:
#         count += 1

# print("Unlilar soni:", count)







# >>>--------------->> 🟣 Expert daraja

"""# N gacha bo'lgan barcha faktoriallar"""

# n = int(input("n ni kiriting: "))

# for k in range(1, n+1):
#     fact = 1
#     for i in range(1, k+1):
#         fact *= i
#     print(f"{k}! = {fact}")
