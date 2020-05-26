# 学习笔记

[TOC]

> 第一题：HashMap小结，几乎无基础，也不熟悉Java，选择不做

| 名称          | 刷题次数 | 更新时间 |
| ------------- | -------- | -------- |
| valid-anagram |          |          |
| twosum        |          |          |
|               |          |          |



## 1. [valid-anagram]( https://leetcode-cn.com/problems/valid-anagram/description/ )

### 四步切题法

- 看题：输入两个字符串，判断两者是否为字母异位词。 异位词的概念是字母个数相同但顺序不同，假定只考虑小写

- 思路：

  - 优先判断特殊情况：两个字符串长度是否相等，如果不等则直接返回 False
  - 然后，进入主体循环
    - 排序后比较。 利用python的排序来对两个字符进行排序，如果两者相等则True
    - 无

- 代码

  - 排序后比较 时间复杂度O(NlogN)

    ```
    class Solution:
        def isAnagram(self, s, t) :
            if len(s) != len(t):
                return False
            s = sorted(s)
            t = sorted(t)
            if s == t:
                return True
            return False
    ```

    同样方法的一行代码实现

    `return sorted(s) == sorted(t)`

- 反馈（忽略调包的方法）

  - leetcode cn找思路, .com python3没找到新思路

    - 先利用set去重后比对两个字符串的相同字符串是否一样，然后再比较个数，最后return

      ```
      class Solution:
          def isAnagram(self, s, t) :
              # 社区中利用set的方式来对比，先用set来确认两个字符串元素都相等，然后进行数量比对
              if len(s) != len(t): return False
              if set(s) == set(t):
                  for i in set(s):
                      if s.count(i) != t.count(i): return False
                  return True
              else:
                  return False
      ```

    - hash的方法 O(n)   利用大小为26的数组做hash表来存，一串字符集+1，另一串字符碰到相同元素-1，若最后若有值<=0，则False 

      ```
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
      
      ```

      

      

       

    



## 2. [twosum]( https://leetcode-cn.com/problems/two-sum/description/ )

之前已经作过了>5遍，这里仅记录最终学到的代码

- 一轮hash解决，每次只在前面存的hash表里面查即可

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 解法三：利用字典hash
        hashmap = {}
        for i,n in enumerate(nums):
            if target -n in hashmap:
                return [i, hashmap.get(target-n)]
            hashmap[n] = i
        return []
```





## 3. [n-ary-tree-preorder-traversal]( https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/ )



## 4. [heapsort自学](  https://www.geeksforgeeks.org/heap-sort/ )



## 5. 



 https://leetcode-cn.com/problems/group-anagrams/
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
https://leetcode-cn.com/problems/chou-shu-lcof/
https://leetcode-cn.com/problems/top-k-frequent-elements/ 