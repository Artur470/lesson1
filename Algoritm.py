



################################ Алгоритмы #########################

#
#
# def  bSort(array):
#     length = len(array)
#     for i in range(length):
#         for j in range(0, length-i-1):
#             if array[j] > array[j+1]:
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
#
# array = [3,4,6,7,5,3,2,4,6,8]
# bSort(array)
# print(array)
#

#
# def bubble_sort(array):
#     n = len(array)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#
#
# numbers = [6,4,3,4,6,7,6,3,9,8,0,1]
# print("исходный массив", numbers)
# bubble_sort(numbers)
# print("Отсортированный массив:", numbers)
#

#
#
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         current_value = arr[i]
#         position = i
#         while position > 0 and arr[position - 1] > current_value:
#             arr[position] = arr[position - 1]
#             position -= 1
#             arr[position] = current_value
#     return arr
# #         4  8
# numbers = [8, 4, 3, 7, 6, 5, 2]
# print("До сортировки:", numbers)
# sorted_numbers = insertion_sort(numbers)
# print("После сортировки:", sorted_numbers)








