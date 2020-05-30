#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        # 第二、三实际思路是一样的，区别只在有没有用dict.get()函数以及key值的确认方法
        # dict = {}
        # for item in strs:
        #     key = tuple(sorted(item))
        #     dict[key] = dict.get(key, []) + [item]
        # return list(dict.values())

        # res = dict()
        # for word in strs:
        #     key = "".join(sorted(word))
        #     if key in res:
        #         res[key].append(word)
        #     else:
        #         res[key]=[word]
        # return list(res.values())

        # # 纯暴力 利用sorted函数来做，匹配到就从原数组删除
        # res = []
        # for word in strs[:]:
        #     lst = []
        #     key = sorted(word)
        #     for item in strs[:]:
        #         if sorted(item) == key:
        #             lst.append(item)
        #             strs.remove(item)

        #     if lst:
        #         res.append(lst)
        # return res

# @lc code=end

