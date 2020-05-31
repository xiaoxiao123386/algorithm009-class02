# 学习笔记

[TOC]

> 第一题：HashMap小结，几乎无基础，也不熟悉Java，选择不做



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

      

      

       

    



## 2. [twosum](https://leetcode-cn.com/problems/two-sum/description/)

之前已经作过了>5遍，这里仅记录最终学到的代码

- 一轮hash解决，每次只在前面存的hash表里面查即可  时间复杂度O(N)

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





## 3. [n-ary-tree-preorder-traversal](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/)

- 看题，知道怎么走，不知道怎么写

- 思路：无

- 代码：直接背+写

  - 递归 

    ```
    
            # first recursion
            if not root: return []
            res = [root.val]
            for i in root.children:
                res += self.preorder(i)
            return res
    ```

  - 加栈

    ```
    		# second: stack
            res = []
            stack = [root]
            while stack:
                node = stack.pop()
                if node:
                    res.append(node.val)
                    for i in node.children[::-1]:
                        stack.append(i)
            return res
    
    ```

    

  - com most vote answer， 在上个方法基础上再优化一些语句

    ```
    		# third: leetcode.com most vote answer
            res, q = [], root and [root]
            while q:
                node = q.pop()
                res.append(node.val)
                q+=[child for child in node.children[::-1] if child]  #优雅的实现
            return res
    
    ```

- 反馈，见上面代码环节



## 4. [heapsort自学]( https://www.geeksforgeeks.org/heap-sort/)

- 简单看了视频，没有深入学习
- **回头第二轮需要再巩固**

## 5. [group-anagrams](https://leetcode-cn.com/problems/group-anagrams/)

- 看题：输入字符串数组、输出：将字符串按异位词同组放一起，只考虑小写字母，不用考虑输出顺序

- 思路：

  - 暴力：依次遍历数组中所有字符串，找出其异位词个数，然后append到结果数组中，中间还要涉及到中间结果的保存和去重操作

    ```
    结果：10分钟内没写出来（写出来的结果不对）
    ```

- 代码：同上

  - 直接看社区答案

    - 暴力法

      ```
              # 纯暴力 利用sorted函数来做，匹配到就从原数组删除
              res = []
              for word in strs[:]:
                  lst = []
                  key = sorted(word)
                  for item in strs[:]:
                      if sorted(item) == key:
                          lst.append(item)
                          strs.remove(item)
      
                  if lst:
                      res.append(lst)
              return res
      
      ```

    - 字典法

      ```
      		res = {}
              for item in strs:
                  key = ''.join(sorted(item))  # 确定唯一的键值，也可以用tuple
                  res[key] = res.get(key, [])+[item] # 也可以用key in dict来判断，但这种明显更优雅
              return list(res.values())
      ```

    - 还有一种素数法，思路比较巧妙，下轮再关注

    

- 反馈：如上

## 6. [binary-tree-inorder-traversal](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)

- 看题，中序遍历，比较直接

- 思路

  - 递归法

- 代码：

  - 递归法 时间复杂度O(2^n)?  空间复杂度O(n)

    ```
    		res = []
            if root:
                res+=self.inorderTraversal(root.left)
                res.append(root.val)
                res+=self.inorderTraversal(root.right)
            return res
    
    ```

- 反馈：

  - 学习迭代法，学习社区的好理解版本

    ```
            # second: iteration with stack
            WHITE, GRAY = 0, 1
            res = []
            stack = [(WHITE, root)]
            while stack:
                color , node = stack.pop()
                if node is None: continue
                if color == WHITE:
                    stack.append((WHITE, node.right))
                    stack.append((GRAY, node))
                    stack.append((WHITE, node.left))
                else:
                    res.append(node.val)
            return res
            
    ```

  - 莫里斯遍历（暂时还没了解，下一轮看视频再补充）

## 7. [binary-tree-preorder-traversal](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)

- 思路跟6是一致的，不再重复记录
- 待办：依然是莫里斯遍历

## 8. [n-ary-tree-level-order-traversal](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/)

- 看题：实现N叉树的层序遍历

- 思路：无

- 代码：无

- 学：

  - 先看一种直接的解法，每次将一层完全走一遍

    ```
    if not root: return []
            level = [root]
            res = []
            
            while level:
                res.append([node.val for node in level])
                level = [child for node in level for child in node.children]
            return res
    ```

- 反馈：先记住这一种方法，等第二轮回来看

  

## 9. [chou-shu-lcof](https://leetcode-cn.com/problems/chou-shu-lcof/)

- 看题：求从1开始数的第n个丑数，丑数的定义：1是，然后后面只包含2、3、5因子的叫丑数，n<=1690

- 思路：

  - 暴力，每给出一个n，从头到尾去判断一遍，找到第n个满足条件的数

- 代码：

  - 暴力：没写出来

    - 看社区 会超时 时间复杂度是O(NlogN)，空间复杂度O(1)

      ```
      class Solution:
          def isugly(self, num):
        if num < 0:
                  return False
          while (num % 2 == 0):
                  num/=2
              while (num % 3 == 0):
                  num/=3
              while (num % 5 == 0):
                  num/=5
              return num==1
          
          
          def nthUglyNumber(self, n: int) -> int:
              count = 0
              res = 1
              while count < n:
                  if self.isugly(res):
                      count+=1
                  res+=1
              return res-1
      ```
      
    - 暴力法太浪费时间，因此可以看生成丑数的规律，如果已知丑数a，那么a*2|3|5也都是丑数，随后利用最小堆heap来做
    
      ```
      import heapq
      
      class Solution:
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
      ```
  
- 反馈，等第二轮再增加

  

## 10.[top-k-frequent-elements](https://leetcode-cn.com/problems/top-k-frequent-elements/ )—— 待完成







