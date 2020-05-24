#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 解法一：切片
        # l = len(nums)
        # k%=l
        # nums[:]=nums[l-k:]+nums[:l-k]

        # 解法二：三次翻转
        # def swap(l,r):
        #     while l < r:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l+=1
        #         r-=1
        # length= len(nums)
        # k%=length
        # swap(0,length-k-1)
        # swap(length-k,length-1)
        # swap(0, length-1)

        # 解法三：Python插入
        n = len(nums)
        k %= n
        for i in range(k):
            nums.insert(0, nums.pop())
# @lc code=end

