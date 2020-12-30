# Bubble Sort Logic (Optimized Solution with break)
# 
# Time Complexity:     
#       Worst Case:                 O(n2)
#       Best Case(Already Sorted):  O(n)
# 
# Space Complexity:                O(1)

def BubbleSort(nums, array_len):
    for i in range(array_len-1):
        flag = False
        for j in range(i+1, array_len):
            if(nums[i] > nums[j]):
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                flag = True
        
        if(not flag):
            break
    print(nums)

nums = []
array_len = int(input("Enter Length of Array: "))
for i in range(array_len):
    num = int(input("Enter number: "))
    nums.append(num)

BubbleSort(nums, array_len)