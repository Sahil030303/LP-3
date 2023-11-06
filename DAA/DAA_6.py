#deterministic quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    #for deterministic pivot element can be the first unsorted element or the element from middle 
    pivot_index = len(arr) // 2  # Choose the middle index as the pivot
    pivot = arr[pivot_index]  # Pivot element

    # Partition the array into three subarrays: less than, equal to, and greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right subarrays
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    # Concatenate the sorted subarrays and the middle elements
    return sorted_left + middle + sorted_right

# Example usage:
my_list = [3, 6, 8, 10, 1, 2, 4]
sorted_list = quick_sort(my_list)
print(sorted_list)

#randomized quick sort
import random

def quick_sort2(arr):
    if len(arr) <= 1:
        return arr

    pivot_index2 = random.randint(0, len(arr) - 1)  # Choose a random pivot index
    pivot2 = arr[pivot_index2]  # Pivot element

    # Partition the array into three subarrays: less than, equal to, and greater than the pivot
    left2 = [x for x in arr if x < pivot2]
    middle2 = [x for x in arr if x == pivot2]
    right2 = [x for x in arr if x > pivot2]

    # Recursively sort the left and right subarrays
    sorted_left2 = quick_sort2(left2)
    sorted_right2 = quick_sort2(right2)

    # Concatenate the sorted subarrays and the middle elements
    return sorted_left2 + middle2 + sorted_right2

# Example usage:
my_list2 = [3, 6, 8, 10, 1, 2, 1]
sorted_list2 = quick_sort2(my_list2)
print(sorted_list2)