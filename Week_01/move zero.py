#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 解法二：双指针滑动，交换非0和0
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
        return nums
        # # 解法三：非零元数替换0元素法
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[j] = nums[i]
        #         if i != j:
        #             nums[i] = 0
        #         j+=1
        # return nums

        # # 解法一：统计0的个数，最后统一append再清除
        # n = nums.count(0)
        # for i in range(n):
        #     nums.append(0)
        #     nums.remove(0)
# @lc code=end

