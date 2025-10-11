''' 10/10/2025 '''

# def list_sum(arr):
#     if len(arr) == 0:
#         return 0
#     else :
#         return arr[0] + list_sum(arr[1:])

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list_sum(arr))




# def binary_search(arr, x):
#     left, right = 0, len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == x:
#             return mid
#         elif arr[mid] <= x:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# arr = [12, 13, 14, 15, 16, 17, 18, 19, 20]
# x = 14
# natija = binary_search(arr, x)
# if natija != -1:
#     print(f"Element: {x} -> Index: {natija}")
# else:
#     print("Bunday element yoq")



# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i

#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
        
#         arr[i], arr[min_index] = arr[min_index], arr[i]

#     return arr

# arr = [12, 45, 90, 34, 56, 72, 13, 65, 14]
# print(selection_sort(arr))



# def linear_search(arr, x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return f"Element: {x} -> Index: {i}"
#     return "Bunday element topilmadi !!!"

# arr_sorted = [1, 2, 3, 4, 5, 6, 7, 8]
# arr_unsorted = [1, 5, 2, 3, 7, 4, 9, 8]
# x= 5
# print(linear_search(arr_sorted, x))
# print(linear_search(arr_unsorted, x))