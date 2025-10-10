''' 04/10/2025 '''

# >>>------------------------------>> ARRAY <<-----------------------------------<<< #

# m1

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(arr[0]) # arr boshidagi elementni chiqaradi.
# print(arr[2]) # arr n- indxda turgan qiymatni chiqaradi.
# print(arr[-1]) # arr da oxirgi elementni chiqaradi.


# m2 

# arr = [12, 13, 14, 15, 16, 17, 18, 19, 20]
# arr.append(12)
# print(arr)

# m3

# arr = [12, 13, 14, 15, 16, 17, 18, 19, 20]
# # arr.remove(arr[0]) # index va qiymati orqali ochiriladi 
# arr.pop(5) # index orqali ochiradi
# print(arr)



# m4

# arr = [12, 13, 14, 15, 16, 17, 18, 19, 20]

# arr[1] = 100
# arr.sort()
# print(arr)



# m5


# arr = [12, 13, 14, 15, 16, 17, 18, 19, 20]
# len = len(arr)
# print(len)







""" ⚙️ 5. Array algoritmik amallari: """

''' Quyida algoritmik nuqtai nazardan muhim amallar keltirilgan: '''

# m1   Elementni izlash (Linear Search)

# arr = [10, 12, 13, 23, 34, 56, 78, 90]
# x= 12
# for i in range(len(arr)):
#     if arr[i] == x:
#         print(f"{x} - element:  {i} - indeksda joylashgan. ")




# m2 Eng katta elementni topish

# arr = [4, 5, 2, 6, 9, 2, 3]
# max_val = arr[0]
# for i in arr:
#     if i > max_val:
#         max_val = i
# print("Eng katta: ", max_val)


# m3 Massivni teskari qilish

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# reversed_arr = arr[::-1]
# print(reversed_arr)


# m4 

# prices = [15000, 23000, 12000, 18000, 27000]

# min_price = prices[0]
# for price in prices:
#     if price < min_price:
#         min_price = price
# print("Eng arzon dori:", min_price)








# >>>---------------------------->> AMALIYOT <<----------------------------------<<< #



''' 🧮 1-masala (Boshlang‘ich) '''
""" Berilgan massivdagi barcha elementlarning yig‘indisini hisobla. """

# arr = [2, 4, 6, 8]
# summa = sum(arr)
# print(summa)



''' 🔢 2-masala (Boshlang‘ich) '''
""" Berilgan massivdagi eng katta va eng kichik elementni top. """

# arr = [15, 2, 8, 25, 9]

# num = arr[0]
# for min in arr:
#     if min < num:
#         num = min
# print(f"Eng kichik: {num}") 

# for max in arr:
#     if max > num:
#         num = max      
# print(f"Eng katta: {num}") 




''' ⚙️ 3-masala (O‘rta) '''
""" Berilgan massivdagi juft sonlar sonini aniqlovchi dastur yoz. """

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 0
# for i in range(len(arr)):
#     if i % 2 == 0:
#         n += 1
#         print(f"Juft son: {arr} ")
# print(f"Natija: {n} marta uchradi. ")



''' 🔁 4-masala (O‘rta – algoritmik) '''
""" Berilgan massivdagi ma’lum son necha marta takrorlanganini hisobla (bunda count() funksiyasidan foydalanma). """


# arr = [2, 3, 2, 5, 2, 4] # >>>----->> I - variant
# n = 0
# for i in range(len(arr)):
#     if arr[i] == 2:
#         n += 1 
# print(f"Natija: {n} marta uchradi. ")

# def nmarta_uchrash(arr, x): # >>>------>> II - variant 
#     n = 0
#     for i in range(len(arr)):
#         if arr[i] == x :
#             n += 1
#     print(f"Natija: {x} soni -> {n} marta uchradi")

# arr = [2, 3, 2, 5, 2, 4]
# x = 2
# nmarta_uchrash(arr, x)




''' 💥 5-masala (Murakkab) '''
""" Berilgan massivni teskari tartibda chiqargan dastur tuz — lekin [::-1] yoki reverse() funksiyasidan foydalanmasdan. """

# arr =[10, 20, 30, 40, 50]
# yangi = []

# for i in range(1, len(arr) + 1):
#     yangi.append(arr[-i])
# print(yangi)




