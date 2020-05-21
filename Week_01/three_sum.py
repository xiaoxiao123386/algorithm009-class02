#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        # 新看到的优秀解法，利用set去重，然后分几种情况考察
        res = set([])

        minus = sorted([n for n in nums if n<0])
        minus_c = set(minus)
        len_0 = nums.count(0)
        plus = sorted([n for n in nums if n>0])
        plus_c = set(plus)

        if len_0 > 2:
            res.add((0,0,0))
        if len_0 > 0:
            for i in range(len(minus)):
                if -minus[i] in plus_c:
                    res.add((minus[i],0,-minus[i]))
        
        n = len(minus)
        for i in range(n):
            for j in range(i+1,n):
                if -(minus[i]+minus[j]) in plus_c:
                    res.add((minus[i],minus[j],-(minus[i]+minus[j])))
        
        n = len(plus)
        for i in range(n):
            for j in range(i+1,n):
                if -(plus[i]+plus[j]) in minus_c:
                    res.add((-(plus[i]+plus[j]),plus[i],plus[j]))
        return list(res)


        # # 优秀解法
        # res = []
        # n = len(nums)
        # #判定特殊情况
        # if not nums or len(nums)<3:
        #     return []
        # nums.sort()
        # for i in range(n):
        #     if nums[i] > 0:
        #         return res
        #     if i > 0 and nums[i]==nums[i-1]:
        #         continue
        #     L = i+1
        #     R = n-1
        #     while L<R:
        #         if nums[i]+nums[L]+nums[R]==0:
        #             res.append([nums[i],nums[L],nums[R]])
        #             while L<R and nums[L]==nums[L+1]:
        #                 L = L+1
        #             while L<R and nums[R]==nums[R-1]:
        #                 R = R-1
        #             L = L+1
        #             R = R-1
        #         elif nums[i]+nums[L]+nums[R]<0:
        #             L = L+1
        #         else:
        #             R = R-1
        # return res



        #暴力解法，超时
        # result = []
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             # print("aa %i %i %i" %(nums[i],nums[j],nums[k]))
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                temp = [nums[i], nums[j], nums[k]]
        #                temp.sort()
        #                if temp in result:
        #                   pass
        #                else:
        #                   result.append(temp)
        # if len(result) == 0:
        #     return []
        # else:
        #     return result
# @lc code=end

b = [-1,0,1,2,-1,-4]

a = Solution()
a.threeSum(b)