# Quick Sort (Divide and Conquer)
# 
# Time Complexity:
#       Best, Avg Case:     O(nlogn)
#       Worst Case:         O(n2)
# 
# Space Complexity:         O(n)

# I'm making two functions in this...
#   One for partitioning
#   Other for Quicksort itself.


def partition(arr, low, high):
    i = low-1
    pivot = arr[high]

    for j in range(low, high):
        if(arr[j] < pivot):
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high):

    if(low < high):
        pi = partition(arr, low, high)

        quicksort(arr, low, pi-1)
        quicksort(arr, pi, high)


array_length = int(input("Enter Array Length: "))
arr = []

for i in range(array_length):
    num = int(input('Enter Number: '))
    arr.append(num)

quicksort(arr, 0, array_length-1)

for i in range(array_length):
    print("%d" %arr[i])