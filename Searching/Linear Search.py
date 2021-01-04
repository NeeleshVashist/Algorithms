# Linear Search

def linear_search(arr, num):
    for i in range(len(arr)):
        if(arr[i] == num):
            return i
    
    return -1


arr = []
array_length = int(input("Enter Array Length: "))

for i in range(array_length):
    num = int(input('Enter Number: '))
    arr.append(num)

num = int(input("Enter Number to Search: "))

index = linear_search(arr, num)

if(index == -1):
    print("Number not found!")
else:
    print("Number found at " + str(index) + " index in array", arr)