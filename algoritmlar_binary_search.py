'''02/10/2025'''

# >>>-------------------------->> 02 Binary search <<----------------------------<<< #


# def binary_search(arr, x):
#     left, right = 0, len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1


# arr = [1, 3, 5, 7, 9, 11, 15, 20]
# x = 8   # Qidiriladigan son

# natija = binary_search(arr, x)

# if natija != -1:
#     print(f"{x} elementi {natija}-indeksta joylashgan.")
# else:
#     print("Element topilmadi.")





# >>>----------------------------->> AMALIYOT <<---------------------------------<<< #


# M1

""" 🟢 1-mashq (Oddiy) """

# def binary_search(arr, x):
#     left, right = 0, len(arr) -1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
        
#     return -1


# arr = [2, 4, 6, 8, 10, 12]
# x = 10

# natija = binary_search(arr, x)
# if natija != -1:
#     print(f"{x} element {natija} - indeksda joylashgan ")
# else:
#     print("Element topilmadi ")



# M2

''' 🟡 2-mashq (Topilmasa) '''

# def binary_search(arr, x):
#     left, right = 0, len(arr) -1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# arr = [1, 3, 5, 7, 9, 11, 13]
# x = 8

# natija = binary_search(arr, x)
# if natija != -1:
#     print(f"{x} element {natija} - indeksda joylashgan. ")
# else:
#     print("Element topilmadi. ")




# M3

""" 🟠 3-mashq (String massiv) """

# def binary_search(arr, x):
#     left, right = 0, len(arr) -1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1

# arr = ["apple", "banana", "cherry", "grape", "mango", "peach"]
# x = "grape"
# natija = binary_search(arr, x)

# if natija != -1:
#     print(f"{x.capitalize()} -> element  {natija} - indexda joylashgan. ")
# else:
#     print("Element topilmadi. ")






# M4

''' 🔵 4-mashq (Ko‘p element qidirish) '''

# def binary_search(arr, x):
#     left, right = 0, len(arr) -1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# arr = [5, 10, 15, 20, 25, 30, 35, 40]
# x = [15, 40, 7]

# #  for i in x: #>>>------------>>  1 - usul
# #     natija = binary_search(arr, i)
# #     if natija != -1:
# #         print(f"{i} - element {natija} - indexda joylashgan. ")
# #     else:
# #         print(f"{i} - Element topilmadi")


# # i = 0 # >>>--------------------->> 2 - usul
# # while i < len(x):
# #     natija = binary_search(arr, x[i])

# #     if natija != -1:
# #         print(f"{x[i]} element {natija} - indexda. ")
# #     else:
# #         print(f"{x[i]} - Element topilmadi. ")
# #     i += 1




# M5

''' 🔴 5-mashq (Murakkabroq – Takroriy elementlar) '''

# def frist_occurrence(arr, x):
#     left, right = 0, len(arr) - 1
#     result = -1
#     while left <= right:
#         mid = (left + right) // 2
        
#         if arr[mid] == x:
#             result = mid
#             right = mid -1
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result

# def last_occurrence(arr, x):
#     left, right = 0, len(arr) - 1
#     result= -1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == x:
#             result = mid
#             left = mid + 1
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result


# arr = [1, 2, 2, 2, 3, 4, 5]
# x = 2 

# birinchi = frist_occurrence(arr, x)
# oxirgi = last_occurrence(arr, x)

# print(f"{x} ning birinchi indeksi = {birinchi}")
# print(f"{x} ning oxirgi indeksi = {oxirgi}")