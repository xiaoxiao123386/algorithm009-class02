#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1

        # # 思路一：不符合题目要求，但可以写一下
        # b = set(nums)
        # c = list(b)
        # return c
        
# @lc code=end

