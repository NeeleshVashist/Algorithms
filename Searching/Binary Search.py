# Binary Search

def binary_search(arr, left_index, right_index, num):
    if(left_index <= right_index):
        mid = left_index + (right_index-1) // 2

        if(arr[mid] == num):
            return mid
        
        elif(arr[mid] > num):
            return binary_search(arr, left_index, mid-1, num)
        
        else:
            return binary_search(arr, mid+1, right_index, num)
    
    else:
        return -1



arr = []
array_length = int(input("Enter Array Length: "))
left_index = 0
right_index = array_length-1

for i in range(array_length):
    num = int(input("Enter Number: "))
    arr.append(num)

num = int(input("Enter Number to Search: "))

index = binary_search(arr, left_index, right_index, num)

if(index == -1):
    print("Number not found!")
else:
    print("Number found at " + str(index) + " in array", arr)