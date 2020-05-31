#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
import heapq

class Solution:
    # def isugly(self, num):
    #     if num < 0:
    #         return False
    #     while (num % 2 == 0):
    #         num/=2
    #     while (num % 3 == 0):
    #         num/=3
    #     while (num % 5 == 0):
    #         num/=5
    #     return num==1
    
    def nthUglyNumber(self, n: int) -> int:
        # ２、 最小堆法，利用heap特性来做
        heap = []
        heapq.heappush(heap, 1)
        seen = set()
        seen.add(1)

        factors = [2, 3, 5]

        curr_ugly = 1
        for _ in range(n):
            curr_ugly = heapq.heappop(heap)
            for j in factors:
                new_ugly = curr_ugly * j
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return curr_ugly
        # 1、暴力法
        # count = 0
        # res = 1
        # while count < n:
        #     if self.isugly(res):
        #         count+=1
        #     res+=1
        # return res-1

       

            


# @lc code=end

