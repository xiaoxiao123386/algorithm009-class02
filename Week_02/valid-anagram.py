class Solution:
    def isAnagram(self, s, t) :
        
        # 利用大小为26的数组做hash表来存，一串字符集+1，另一串字符碰到相同元素-1，若最后若有值<=0，则False
        if len(s) != len(t): return False
        counts = [0]*26
        for a in s:
            counts[ord(a) - ord('a')] += 1
        for b in t:
            # 前面已经确认过长度一样了，因此如果不同一定有<=0的情况出现，之所以条件有=0是因为-1在判断后面操作
            if counts[ord(b) - ord("a")] <=0:
                return False
            counts[ord(b) - ord("a")]-=1
            
  
        return True
        


        # # 社区中利用set的方式来对比，先用set来确认两个字符串元素都相等，然后进行数量比对
        # if len(s) != len(t): return False
        # if set(s) == set(t):
        #     for i in set(s):
        #         if s.count(i) != t.count(i): return False
        #     return True
        # else:
        #     return False

        # # 利用sorted方法排序，然后比较的方式
        # if len(s) != len(t):
        #     return False
        # s = sorted(s)
        # t = sorted(t)
        # if s == t:
        #     return True
        # return False
        # 一句话的形式
        # return sorted(s) == sorted(t)