''' 12/10/2025 '''

# def bubblesort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#             print(arr)
#     return arr
        
# nums = [1, 12, 2, 13, 3, 14, 4, 15, 51]
# print(bubblesort(nums))


# m1.1 

# def bubblesort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# nums = [12, 1, 2, 3, 13, 23, 21, 22, 56, 34, 5]
# print(bubblesort(nums))



# m1.2


# def bubblesort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# nums = [12, 13, 21, 32, 23,4, 5, 54, 45 ]
# print(bubblesort(nums))




# m1.3

# def bubblesort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# nums = [78, 8, 7, 90, 6, 5, 65, 45, 5, 34, 2, 1]
# print(bubblesort(nums))




""" 🧩 1-masala (Boshlang‘ich) """
''' Berilgan ro‘yxatni Bubble Sort yordamida o‘sish tartibida saralang. '''

# def bubblesort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# nums = [9, 2, 5, 1, 6]
# print(bubblesort(nums))


""" 🧩 2-masala (O‘rtacha) """
''' Berilgan ro‘yxatni Bubble Sort yordamida kamayish tartibida saralang
(ya’ni eng kattadan eng kichikkacha). '''

# def bubblesort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - i - 1):
#             if arr[j] < arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# nums = [4, 7, 2, 9, 1]
# print(bubblesort(nums))



""" 🧩 3-masala (Amaliy) """
''' Foydalanuvchidan 5 ta son kiritishni so‘rang,
ularni ro‘yxatga joylab, Bubble Sort yordamida saralang. '''

# def bubblesort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr
# arr = []
# n = 0
# len1 = int(input("Royxat elementlar soni nechtadan iborat bolsin: "))
# while n < len1:
#     nums = int(input("Kiritish: "))
#     arr.append(nums)
#     n += 1

# print(bubblesort(arr))





""" 🧩 4-masala (Optimallashtirish) """
''' Massiv allaqachon tartiblangan bo‘lsa, keraksiz sikllarni to‘xtatadigan versiyani yozing. '''

# def bubblesort(arr):
#     for i in range(len(arr)):
#         sweeped = False
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 sweeped = True
#         print(arr)
#         if not sweeped:
#             print(f"To'xtadi {i + 10} - iteratsiyada (keraksiz sikl yo'q)")
#             break
#     return arr



# arr = [1, 2, 3, 4, 5]
# print(bubblesort(arr))






""" 🧩 5-masala (Murakkab) """
''' Berilgan ro‘yxatda faqat juft sonlarni Bubble Sort yordamida saralang, toq sonlar esa o‘z joyida qolsin. '''

# def bubblesort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - i - 1):
#             if arr[j] % 2 == 0 and arr[j+1] % 2 == 0 and arr[j]  > arr[j+1]:
#                 arr[j] , arr[j+1] = arr[j+1], arr[j]
#         print(arr)
#     return arr

# nums = [9, 4, 7, 2, 5, 6]
# print(bubblesort(nums))




""" 🔍 Bubble Sort — Vizual versiya """

# def bubblesort_visual(arr):
#     print(f"Boshlang'ich ro'yxat: {arr}\n")

#     for i in range(len(arr) - 1):
#         print(f"➡️  {i+1} - iteratsiya boshlandi")
#         swapped = False

#         for j in range(len(arr) - i - 1):
#             print(f" Taqqoslash: {arr[j]} va {arr[j+1]}", end=" ")
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#                 print(f"👉 almashtirish -> {arr}")
#             else:
#                 print("✅ joyi to‘g‘ri")

#         print(f"🔹 {i+1}-iteratsiya yakuni: {arr}\n")

#         if not swapped:
#             print(f"✅ Massiv {i+1}-iteratsiyada to‘liq tartiblandi.\n")
#             break
              
#     print(f"📊 Yakuniy natija: {arr}")

# nums = [9, 2, 5, 1, 6]
# print(bubblesort_visual(nums))