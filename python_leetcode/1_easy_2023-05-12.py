class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i,n in enumerate(nums):
            if n in dict:
                return dict[n], i
            else:
                dict[target - n] = i
    
nums = [2,7,11,15]
target = 9

sltn = Solution()
print(sltn.twoSum(nums, target))