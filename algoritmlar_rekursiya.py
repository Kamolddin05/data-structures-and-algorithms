'''08/10/2025'''

# m1

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))




# m2

# def fibonachi(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonachi(n-1) + fibonachi(n - 2)

# for i in range(6):    
#     print(fibonachi(i), end=" ")





# m3

# def sumList(arr):
#     if len(arr) == 0:
#         return 0
#     else:
#         return arr[0] + sumList(arr[1:])
    
# print(sumList([2, 3, 4, 5, 6, 7, 8]))






""" 🧮 1-masala (Boshlang‘ich): Raqamlar yig‘indisi """

# def sumL(n):
#     if n == 0:
#         return 0
#     else:   
#         son = n % 10
#         natija = n // 10
#         return son + sumL(natija)
    
# n= int(input("n= "))
# print(sumL(n))



""" 🔢 2-masala (O‘rta): Listdagi elementlar yig‘indisi """

# def list_sum(arr):
#     if len(arr) == 0 :
#         return 0
#     else:
#         return arr[0] + list_sum(arr[1:])
    
# arr = [2, 4, 6, 8]
# print(f"Natija: {list_sum(arr)}")




""" 🧠 3-masala (O‘rta): Fibonachchi sonini topish """


# def fibonachi(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonachi(n-1) + fibonachi(n-2)
    
# n= int(input("n= "))
# print(fibonachi(n))




""" 🪜 4-masala (Murakkab): Sonlar ketma-ketligini teskari chiqarish """

# def teskari(n):
#     if n == 1:
#         return 1
#     else:
#         son = n % 10
#         natija = n // 10
#         return int(str(son) + str(teskari(natija)))
    
# n= int(input("n= "))
# print(teskari(n))




""" 🧩 5-masala (Murakkab): Ro‘yxat ichidagi maksimal qiymatni topish """

# def max_element(arr):
#     if len(arr) == 1:
#         return arr[0]
    
#     if arr[0] > max_element(arr[1:]):
#         return arr[0]
#     else:
#         return max_element(arr[1:])
    
# arr = [10, 5, 40, 25, 7]
# print(max_element(arr))
