#deterministic quick sort
def partition(array, low, high):
    pivot = array[low]
    i = low + 1
    j = high
    while True:
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] >= pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            break
    array[low], array[j] = array[j], array[low]
    return j

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

data = [1, 7, 4, 10, 9, -2, 0, -2, 4, 11]
print("Unsorted Array")
print(data)

size = len(data)
quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)