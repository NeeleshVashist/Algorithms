# Merge Sort (Divide and Conquer)
# 
# Time Complexity:
#       Best, Avg, Worst Case:      O(nlogn)
# 
# Space Complexity:                 O(n)

def MergeSort(array):
    array_length = len(array)
    
    if(array_length > 1):
        left_array = array[:array_length//2]
        right_array = array[array_length//2:]

        # Recursive Calls 

        MergeSort(left_array)
        MergeSort(right_array)

        # i = index for left_array
        # j = index for right_array
        # k = index for array

        i = j = k = 0
        
        while(i < len(left_array) and j < len(right_array)):
            if(left_array[i] < right_array[j]):
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            
            k += 1
        
        while(i < len(left_array)):
            array[k] = left_array[i]
            i += 1
            k += 1

        while(j < len(right_array)):
            array[k] = right_array[j]
            j += 1
            k += 1



array = []
array_length = int(input("Enter Array Length: "))

for i in range(array_length):
    num = int(input('Enter Number: '))
    array.append(num)

MergeSort(array)
print(array)