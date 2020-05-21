#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 解法三：利用字典hash
        hashmap = {}
        for i,n in enumerate(nums):
            if target -n in hashmap:
                return [i, hashmap.get(target-n)]
            hashmap[n] = i
        return []

        # # 解法二 求 target - num1
        # for i in range(len(nums)):
        #     if target - nums[i] in nums[i+1:]:
        #         return [i, nums.index(target - nums[i], i+1)]
        # return []

        # # 解法一 暴力
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []
        
# @lc code=end

