'''03/10/2025'''

# >>>------------------------------->> Big(O) <<---------------------------------<<< #

# Big(O) tahlil

# m1

""" 🟢 1-mashq — O(1): Doimiy vaqt algoritmi """
''' 👉 Har doim bitta amal bajariladi, n o‘lchamidan qat’i nazar. '''

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def get_frist_element(a):  # >>>------>> 🧠 Tahlil: faqat bitta element olinadi → O(1)
#     return a[2]

# print(get_frist_element(arr))    


# m2

""" 🟡 2-mashq — O(n): Chiziqli vaqt """
''' 👉 Har bir elementni bitta-bitta ko‘rib chiqadi. '''

# def find_element(arr, x):  # >>>------>> 🧠 Tahlil: har bir element tekshiriladi → O(n)
#     for i in arr:
#         if i == x:
#             return True
#     return False

# print(find_element([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))


# m3

""" 🔵 3-mashq — O(log n): Binary Search """
''' 👉 Har qadamda massiv yarmiga bo‘linadi. '''

# def binary_search(arr, x):  # >>>------>> 🧠 Tahlil: massiv yarmiga bo‘linadi → O(log n)
#     left, right = 0, len(arr) -1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid -1

#     return -1

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = 1
# natija = binary_search(arr, x)

# if natija != -1:
#     print(f"{x} - Element  {natija} - Indexda joylashgan. ")
# else:
#     print(f"{x} - Element arr da topilmadi. ")






# m4

""" 🟠 4-mashq — O(n²): Kvadrat murakkablik """
''' 👉 Ichma-ich ikki sikl. '''

# def print_pairs(arr): # >>>------>> 🧠 Tahlil: har bir element har biri bilan taqqoslanadi → O(n²)
#     for i in arr:
#         for j in arr:
#             print(i, j)

# print_pairs([1, 2, 3, 4, 5])






# m5

""" 🔴 5-mashq — O(2ⁿ): Eksponensial murakkablik """
''' 👉 Har bir chaqiruv ikki marta o‘zini chaqiradi (rekursiya). '''

def fib(n): # >>>------>> 🧠 Tahlil: har bir chaqiruv ikki bo‘linadi → O(2ⁿ)
    if n <=1:
        return n
    return fib(n-1) + fib(n - 2)

print(fib(21))




# O(1)  → juda tez
# O(log n) → tez
# O(n)  → o‘rtacha
# O(n²) → sekin
# O(2ⁿ) → juda sekin
# O(n!) → imkonsiz darajada sekin
