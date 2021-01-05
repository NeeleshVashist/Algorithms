# Selection Sort Logic
# 
# Time Complexity:     O(n2)
# Space Complexity:    O(1)

def SelectionSort(nums, array_len):
    for i in range(array_len):
        max_num = i
        for j in range(i+1, array_len):
            if(nums[max_num] > nums[j]):
                max_num = j
        
        nums[i], nums[max_num] = nums[max_num], nums[i]

    print(nums)

nums = []
array_len = int(input("Enter Length of Array: "))
for i in range(array_len):
    num = int(input("Enter number: "))
    nums.append(num)

SelectionSort(nums, array_len)