'''12/10/2025'''

# def mergesort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = mergesort(arr[:mid])
#     right = mergesort(arr[mid:])

#     i = j = k = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             arr[k] = left[i]
#             i += 1
#         else:
#             arr[k] = right[j]
#             j += 1
#         k += 1

#     while i < len(left):
#         arr[k] = left[i]
#         i += 1
#         k += 1

#     while j < len(right):
#         arr[k] = right[j]
#         j += 1
#         k += 1

#     return arr  


# arr = [12, 1, 2, 13, 3, 4, 34, 54, 32, 123, 67, 56]
# print("Saralangan:", mergesort(arr))


# def mergesort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr) // 2
#     left = mergesort(arr[:mid])
#     right = mergesort(arr[mid:])
#     res = []
    
#     while left and right:
#         res.append(left.pop(0) if left[0] < right[0] else right.pop(0))
#     return res + left + right

# arr = [12, 1, 2, 13, 3, 4, 34, 54, 32, 123, 67, 56]

# print(mergesort(arr))



# def mergesort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     else:

#         mid = len(arr) // 2
#         left = mergesort(arr[:mid])
#         right = mergesort(arr[mid:])
#         res = []

#         while left and right:
#             if left[0] < right[0]:
#                 res.append(left.pop(0))
#             else:
#                 res.append(right.pop(0))
#         return res + left + right

# arr = [12, 1, 2, 13, 3, 4, 34, 54, 32, 123, 67, 56]
# print(mergesort(arr))



# def mergesort(arr):
#     if len(arr) <=1:
#         return arr
    
#     else:
#         mid = len(arr) // 2
#         left = mergesort(arr[:mid])
#         right = mergesort(arr[mid:])
#         res = []

#         while left and right:
#             if left < right:
#                 res.append(left.pop(0))
#             else:
#                 res.append(right.pop(0))
#         return res + right + left
    

# arr = [12, 1, 2, 13, 3, 4, 34, 54, 32, 123, 67, 56]
# print(mergesort(arr))




''' 🧠 1-masala (Boshlang‘ich) '''
""" Berilgan ro‘yxatni mergesort() yordamida o‘sish tartibida saralang. """

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    else:
        mid = len(arr) // 2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
        res = []

        while left and right:
            if left[0] < right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        return res + left + right
    
arr = [9, 2, 8, 4, 7, 3]
print(mergesort(arr))



''' 🧠 2-masala (Tushuncha mustahkamlash) '''
''' Ro‘yxatdagi manfiy sonlar va musbat sonlarni alohida saralang,
so‘ng ularni birlashtiring (avval manfiylar, keyin musbatlar).
Saralash faqat mergesort() yordamida bajarilsin.'''

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    else:
        minus = []
        plus = []
        for i in range(len(arr)):
            if arr[i] < 0:
                minus.append(arr[i])
            else:
                plus.append(arr[i])
        
        mid1 = len(minus) // 2
        mid2 = len(plus) // 2

        left1 = mergesort(minus[:mid1])
        right1 = mergesort(minus[mid1:])

        left2 = mergesort(plus[:mid2])
        right2 = mergesort(plus[mid2:])

        res_minus = []
        res_plus = []

        while (left1 and right1):

            if left1[0] < right1[0]:
                res_minus.append(left1.pop(0))
            else:
                res_minus.append(right1.pop(0))

        while (left2 and right2):

            if left2[0] < right2[0]:
                res_plus.append(left2.pop(0))
            else:
                res_plus.append(right2.pop(0))

        return (res_minus + left1 + right1) + (res_plus  + left2 + right2)

    

arr = [3, -5, 2, -1, 0, -7, 6]
print(mergesort(arr)) 




''' 🧠 4-masala (Murakkabroq) '''
""" Berilgan sonlar ro‘yxatini teskari tartibda saralang
(mergesort() yordamida)."""


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    else:
        mid = len(arr) // 2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
        res = []

        while left and right:
            if left < right:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        return res + left + right

names = ["Ali", "Bekzod", "Javohir", "Sardor", "Dilshod"]
print(mergesort(names))






''' 🧠 4-masala (Murakkabroq) '''
""" Berilgan sonlar ro‘yxatini teskari tartibda saralang
(mergesort() yordamida). """

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    else:
        mid = len(arr) // 2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
        res = []
        
        while left and right:
            if left[0] > right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        return res + left + right

arr = [10, 3, 5, 8, 1, 9]
print(mergesort(arr))




''' 🧠 5-masala (Yuqori daraja) '''

""" Ro‘yxatda juft va toq sonlarni ajrating,
ikkisini alohida mergesort() bilan saralang,
so‘ng yakuniy natijani quyidagicha chiqaring: """



def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    else:
        juft = []
        toq = []
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                juft.append(arr[i])
            else:
                toq.append(arr[i])

        mid1 = len(juft) // 2
        mid2 = len(toq) // 2

        left1 = mergesort(juft[:mid1])
        right1 = mergesort(juft[mid1:])
        res1 = []
        
        left2 = mergesort(toq[:mid2])
        right2 = mergesort(toq[mid2:])
        res2 = []


        while (left1 and right1):

            if left1[0] < right1[0]:
                res1.append(left1.pop(0))
            else:
                res1.append(right1.pop(0))
        # return res1 + left1 + right1 
        
        while (left2 and right2):
    
            if left2[0] < right2[0]:
                res2.append(left2.pop(0))
            else:
                res2.append(right2.pop(0))
        # return res2 + left2 + right2

        return (res1 + right1 + left1)  + (res2  + right2 + left2)


arr = [7, 4, 9, 2, 6, 3, 10, 1]
print(mergesort(arr))