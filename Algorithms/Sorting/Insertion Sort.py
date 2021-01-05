# Insertion Sort
# 
# Time Complexity:
#       Best Case(Already Sorted):  O(n)
#       Worst Case:                 O(n2)
# 
# Space Complexity:                 O(1)

def InsertionSort(nums, array_len):
    
    for i in range(array_len):
        key = nums[i]
        j = i-1

        while(j>=0 and key<nums[j]):
            nums[j+1] = nums[j]
            j -= 1
        
        nums[j+1] = key

    print("Sorted Array: ", nums)


nums = []
array_len = int(input('Enter Array Length: '))

for i in range(array_len):
    num = int(input('Enter Number: '))
    nums.append(num)

InsertionSort(nums, array_len)