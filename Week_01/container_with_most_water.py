#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        ans = (j - i) * min(height[i], height[j])
        while i < j:
            if height[i] > height[j]:
                ans = max(ans, height[j]* (j-i))
                j-=1
            else:
                ans = max(ans, height[i] * (j-i))
                i+=1
        return ans
            

        
        # ans = 0
        # for i in range(len(height)-1):
        #     for j in range(len(height)):
        #         temp = min(height[i], height[j])*(j-i)
        #         ans = max(ans, temp)
        # return ans

# @lc code=end

