'''07/10/2025'''

#  m1
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i

#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
        
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr


# nums= [5, 3, 6, 7, 9, 2, 1, 8]
# print(selection_sort(nums))




# m2
''' 🧮 1️⃣ Boshlang‘ich daraja '''
""" Masala: Quyidagi ro‘yxatni selection sort algoritmi orqali o‘sish tartibida sarala:"""

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_indexs = i

#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_indexs]:
#                 min_indexs = j

#         arr[i], arr[min_indexs] = arr[min_indexs], arr[i]
#     return arr

# nums = [9, 4, 6, 2, 7]
# print(selection_sort(nums))





# m3

''' 🧠 2️⃣ O‘rta daraja '''
""" Masala: Selection sort yordamida ro‘yxatni kamayish tartibida (descending) sarala: """

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i

#         for j in range(i + 1, len(arr)):
#             if arr[j] > arr[min_index]:
#                 min_index = j

#         arr[i], arr[min_index] = arr[min_index], arr[i]

#     return arr

# nums= [5, 1, 9, 3, 8, 2]
# print(selection_sort(nums))




# m4
''' ⚙️ 3️⃣ Amaliy algoritmik topshiriq'''
""" Selection sortdan foydalangan holda 2 o‘lchovli ro‘yxatni (matritsani) har bir qatordagi elementlar yig‘indisi bo‘yicha o‘sish tartibida sarala. """

# def selection_sort(matrix):
#     for i in range(len(matrix)):
#         min_index = i

#         for j in range(i + 1, len(matrix)):
#             if sum(matrix[j]) < sum(matrix[min_index]):
#                 min_index = j

#         matrix[i], matrix[min_index] = matrix[min_index], matrix[i]
#     return matrix

# matrix = [
#     [3, 5, 2],
#     [1, 1, 1],
#     [4, 2, 6]
# ]
# print(selection_sort(matrix))


# matrix = [
#     [3, 5, 2],
#     [1, 1, 1],
#     [4, 2, 6]
# ]
# print(len(matrix))


# m5 
''' 🔥 4️⃣ Murakkab (fikrlashni kuchaytiruvchi) '''

""" Selection sort algoritmini shunday yozingki, u manfiy sonlar bilan ham ishlasin va natijada barcha elementlar o‘sish tartibida saralansin. """


# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i

#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j

#         arr[min_index], arr[i] = arr[i], arr[min_index]
#     return arr

# nums= [7, -2, 5, 0, -9, 3]
# print(selection_sort(nums))



# |/////////////////////| 🧮 Selection Sort — 10 ta amaliy mashq |\\\\\\\\\\\\\\\\\\\|


# m1 

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i

#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j

#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr

# nums = [8, 1, 6, 3, 5, 9, 2]
# print(selection_sort(nums))


# m2

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i

#         for j in range(i+1, len(arr)):
#             if arr[j] > arr[min_index]:
#                 min_index = j

#         arr[i], arr[min_index] = arr[min_index], arr[i]

#     return arr

# nums= [10, 4, 7, 1, 9, 2]
# print(selection_sort(nums))



# m3

# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         min_index = i

#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
        
#         arr[i], arr[min_index] = arr[min_index], arr[i]

#         print(arr)

# nums= [5, 4, 3, 2, 1]
# selection_sort(nums)


# m4 

# def selection_sort(marix):
#     for i in range(len(marix)):
#         min_index = i

#         for j in range(i+1, len(marix)):
#             if sum(marix[j]) < sum(marix[min_index]):
#                 min_index = j

#         marix[i], marix[min_index] = marix[min_index], marix[i]
#     return marix

# matrix = [
#     [1, 5, 3],
#     [4, 4, 4],
#     [2, 1, 0]
# ]
# print(selection_sort(matrix))
    



# m5

# def selection_sort(arr):
#     for i in range(len(arr)):
#         if arr[i] % 2 == 1:
#             min_index = i 

#             for j in range(i+1, len(arr)):
#                 if arr[i] % 2 == 1:
#                     if arr[j] < arr[min_index]:
#                         min_index = j 

#             arr[i], arr[min_index] = arr[min_index], arr[i]

#     return arr

# nums = [8, 5, 2, 3, 7, 6, 1]
# print(selection_sort(nums))

""" # list= [8, 5, 2, 3, 7, 6, 1]

# for i in range(len(list)): 
#     if list[i] % 2 == 1:   # >>>----------------->> mano shu yerda 
#         print(i) """


# m6

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i

#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j

#         arr[i], arr[min_index] = arr[min_index], arr[i]

#     return arr

# nums = [3, -1, -5, 4, 2, -2]
# print(selection_sort(nums))




# m7

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i

#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]

#     return arr

# world = ["olma", "banan", "shaftoli", "anjir", "nok"]
# print(selection_sort(world))





# m8

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i

#         for j in range(i+1, len(arr)):
#             if arr[j] ** 2 < arr[min_index] ** 2:
#                 min_index = j

#         arr[i], arr[min_index] = arr[min_index], arr[i]

#     return arr

# nums_kv= [-3, 1, -4, 2, 0]
# print(selection_sort(nums_kv))
 



# m9

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i

#         for j in range(i+1, len(arr)):
#             if sum(map(int, str(arr[j]))) < sum(map(int, str(arr[min_index]))):
#                 min_index = j
#         arr[i], arr[min_index], = arr[min_index], arr[i]

#     return arr

# nums_sum = [56, 12, 99, 33, 80]
# print(selection_sort(nums_sum))





# m10

# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         min_index = i

#         for j in range(i+1, len(arr)):
#             if arr[j] > arr[min_index]:
#                 min_index = j
        
#         arr[i], arr[min_index] = arr[min_index], arr[i]

#     return arr[::-1]

# nums = [4, 9, 1, 3, 8]
# print(selection_sort(nums)) 



''' 🧮 m11 – Median topish (selection sort orqali) '''


# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr

# def median_find(nums):
#     sorted_nums = selection_sort(nums[:])
#     n = len(sorted_nums)
#     if n % 2 == 1:
#         return sorted_nums[n // 2]
#     else:
#         return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    
# numbers = [9, 2, 5, 7, 1, 6]
# print("Tartiblangan:", selection_sort(numbers[:]))
# print("Median:", median_find(numbers))




""" 🏆 m12 – Eng katta 3 ta elementni ajratish (selection sort orqali) """


# def selection_sort(arr):
#     for i in range(len(arr)):
#         max_index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] > arr[max_index]:
#                 max_index = j
#         arr[i], arr[max_index] = arr[max_index], arr[i]
#     return arr


# def top_three(nums):
#     sorted_nums = selection_sort(nums[:])
#     return sorted_nums[:3]   # faqat eng katta 3 ta qiymatni olamiz


# nums = [4, 9, 1, 7, 3, 6, 8]
# print("Eng katta 3 ta son:", top_three(nums))



""" 🔢 m13 – Ikki ro‘yxatni birlashtirib tartiblash """



# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr


# def merge_and_sort(list1, list2):
#     combined = list1 + list2   # ikkisini birlashtiramiz
#     return selection_sort(combined)


# a = [5, 2, 8]
# b = [7, 1, 4]
# print("Birlashtirilgan va tartiblangan:", merge_and_sort(a, b))


""" stop """