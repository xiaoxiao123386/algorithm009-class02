#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 解法三：公式法，直接套用公式求解
        import math
        sqrt5 = 5**0.5
        fibin=math.pow((1+sqrt5)/2,n+1)-math.pow((1-sqrt5)/2,n+1)
        return int(fibin/sqrt5)


        # 用代码翻译手动推导的规律  时间复杂度O(n),空间复杂度O(n)
        # climb = {}
        # climb[0] = 0
        # climb[1] = 1
        # climb[2] = 2

        # for i in range(3, n+1):
        #     climb[i] = climb[i-1] + climb[i-2]
        
        # return climb[n]


        # 解法一：对官方动态规划方法的修改 时间复杂度O(n)，空间复杂度O(1)
        # fc = 1
        # sc = 2
        # res = 0
        # for i in range(2, n):
        #     res = fc + sc

        #     fc = sc
        #     sc = res
        # return max(n, res)
# @lc code=end

