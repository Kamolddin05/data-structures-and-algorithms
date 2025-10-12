''' 11/10/2025 '''

# from random import randrange

# def qsort(arr):
#     if len(arr) <=1:
#         return arr
#     else:
#         pivot = arr.pop(randrange(len(arr)))
#         kichik = [i for i in arr if i <= pivot]
#         katta = [i for i in arr if i > pivot]
#         return qsort(kichik) + [pivot] + qsort(katta)
    

# arr = [1, 5, 12, 0, -5, 66]
# print(arr)
# print(qsort(arr))



# m1 
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[-1]
#     left = [x for x in arr[: -1] if x <= pivot]
#     right = [x for x in arr[: -1] if x > pivot]
#     return quicksort(left) + [pivot] + quicksort(right)

# nums = [8, 3, 1, 7, 0, 10, 2]
# sorted_nums = quicksort(nums)
# print(sorted_nums)



# m1.1

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr.pop(0)
#     left = [i for i in arr if i <= pivot]
#     right = [i for i in arr if i > pivot]

#     return quicksort(left) + [pivot] + quicksort(right)

# nums = [1, 5, 2, 3, 7, 8, 0, 9, 4]
# sorted_nums = quicksort(nums)
# print(sorted_nums)



# m1.2

# from random import randrange

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     else:
#         pivot = arr.pop(randrange(len(arr)))
#         left = [x for x in arr if x <= pivot]
#         right = [x for x in arr if x > pivot]
#         # print(f"{quicksort(left)} + {[pivot]} + {quicksort(right)}")
#         return quicksort(left) + [pivot] + quicksort(right)
    
# nums = [1, 5, 2, 7, 8, 3, 9, 2]
# print(quicksort(nums))



""" 🧩 1-masala (Boshlang‘ich) """

''' Berilgan massivni quicksort yordamida o‘sish tartibida saralang. '''

# from random import randrange
# def qucksort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     else:
#         pivot = arr.pop(randrange(len(arr)))
#         left = [x for x in arr if x <= pivot]
#         right = [x for x in arr if x > pivot]
#         return qucksort(left) + [pivot] + qucksort(right)
    
# nums = [12, 1, 3, 5, 13, 45, 67, 23, 32 ,90, 7, 8]
# print(qucksort(nums))



""" 🧠 2-masala (O‘rta daraja) """
''' Quicksort yordamida kamayish tartibida saralovchi funksiya yozing. '''


# from random import randrange
# def quicksort(arr):

#     if len(arr) <= 1:
#         return arr
    
#     else:
#         pivot = arr.pop(randrange(len(arr)))
#         left = [x for x in arr if x >= pivot]
#         righ = [x for x in arr if x < pivot]

#         return quicksort(left) + [pivot] + quicksort(righ)
    
# nums = [7, -2, 10, 4, 3]
# print(quicksort(nums))




""" ⚙️ 3-masala (Amaliy) """
''' Quicksort algoritmini yozing, lekin pivot sifatida massivning o‘rtasidagi elementni tanlang (tasodifiy emas). '''



# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     else:
#         pivot = arr.pop((len(arr)) // 2)
#         left = [x for x in arr if x <= pivot]
#         right = [x for x in arr if x > pivot]
#         # print(f"{quicksort(left)} + [{pivot}] + {quicksort(right)}")
#         return quicksort(left) + [pivot] + quicksort(right)
    
# nums = [11, 3, 5, 2, 8, 7]
# print(quicksort(nums))




""" 🔬 4-masala (Murakkab) """
''' Quicksort algoritmidan foydalangan holda, ro‘yxatdagi takrorlanuvchi elementlarni ham to‘g‘ri tartibda saqlaydigan dastur yozing. '''

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr.pop(0)
#         # print(pivot)
#         left = [x for x in arr if x <= pivot]
#         right = [x for x in arr if x > pivot]
#         return quicksort(left) + [pivot] + quicksort(right)
    
# nums = [5, 3, 8, 9, 1, 5, 8, 3, 9, 1]
# print(quicksort(nums))
 