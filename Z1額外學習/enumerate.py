#enumerate用法  (會取出陣列中的索引和元素)

# 題目：給定一個整數陣列 nums 和一個目標值 target，找出 nums 中的兩個數字，使它們的和等於 target。
# 並返回它們的索引。假設每個輸入只會有一個解，且同一個元素不能使用兩次。


class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i

# 測試程式碼
solution = Solution()

# 測資 1
nums = [2, 7, 3, 15]
target = 10
print(solution.twoSum(nums, target)) 

# 測資 2
nums = [3, 2, 4, 5]
target = 8
print(solution.twoSum(nums, target)) 

# 測資 3
nums = [3, 3, 1, 9]
target = 9
print(solution.twoSum(nums, target))  
