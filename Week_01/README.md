学习笔记

[TOC]



# swapPairs

- 先看题目，输入输出很明确，看起来也没有什么坑

- 思路：知道怎么做，但不知道代码怎么写

- 代码：略

- 背代码、理解(这里只涉及到一种三指针，没有深入，因为发现写错作业了-_-!):

  ```
          thead = ListNode(-1)
          thead.next = head
          c = thead
          while c.next and c.next.next:
              a = c.next
              b = c.next.next
              c.next = b
              a.next = b.next
              b.next = a
  
              c = c.next.next
          return thead.next
  
  ```

  

# reversed_linked_list

- 先看题目，输入输出很明确，看起来也没有什么坑

- 思路：知道怎么做，但不知道代码怎么写

- 代码：略

- 背代码、理解(这里涉及到三种方式,国际站暂时没有看到新的思路):

  - 迭代（双指针，时间复杂度O(n)，空间复杂度O(1)）

    ```
    		cur = None
            pre = head
            while pre:
                tmp = pre.next
                pre.next = cur 
                cur = pre
                pre = tmp
            return cur
    ```

  - 递归

    - 思路：大问题分解为相同求解思路的小问题，然后找到终止条件（空链表或单节点链表）

      ```
              # 第二种解法，递归实现
              if not head or not head.next:
                  return head
              newHead = self.reverseList(head.next)
              head.next.next = head
              head.next = None
              return newHead
      ```

  - 妖魔化的双指针

    - 思路： 原链表的头结点就是反转之后链表的尾结点，使用 head标记，不断的将它的next往右移直到链表尾部。 cur就在head.next之后一直往右移一直到这新head，然后返回cur

      ```
              if head == None:
                  return None
              cur = head
              while head.next:
                  tmp = head.next.next  # 存下一步该指向的节点
                  head.next.next = cur  # 新链表的对应关系确定
                  cur = head.next       # 不断右移指针
                  head.next = tmp       # 移动head.next到下一个位置
      
              return cur
      
      ```

      

  

- 反馈，重复做

# climb_stairs(> 1 times)

- 先看题目，给出楼梯总数和走的方法，要求输入n，输出按给定方法走的方案

- 思路

  - 先找规律，从n=1，走到n=4，基本是规律就是f(n) = f(n-1) + f(n-2)

  - 没有其它思路，接下来就是写代码了

- 代码，基础比较薄弱，没有真正从思路到翻译代码的过程

- 反馈

  - cn社区看，收集到三种方法(除了公式法，都自己又写了一遍)

    - 第一种：我自己没实现的那种 时间、空间复杂度都是O(n)

      ```
              climb = {}
              climb[0] = 0
              climb[1] = 1
              climb[2] = 2
      
              for i in range(3, n+1):
                  climb[i] = climb[i-1] + climb[i-2]
              return climb[n]
      
      ```

    - 第二种，用for循环来实现递归  时间O(n) 空间O(1)

      ```
      		fc = 1
              sc = 2
              res = 0
              for i in range(2, n):
                  res = fc + sc
      
                  fc = sc
                  sc = res
              return max(n, res)
      ```

    - 第三种，公式法。 直接用数列的公式来写代码

      ```
              import math
              sqrt5 = 5**0.5
              fibin=math.pow((1+sqrt5)/2,n+1)-math.pow((1-sqrt5)/2,n+1)
              return int(fibin/sqrt5)
      
      ```

  - com社区，暂时没看到新的思路，下一遍再找找



# container_with_most_water(>2 times)

- 同样先看题目：给出一串坐标>2，最后输出能容纳最多水的容器，输出值一定有一个，没看到什么坑

- 思路：

  - 1. 暴力，两重循环将所有值求出来然后求最大值
    2. 无

- 代码：

  - 暴力法  时间复杂度 O(n^2)  空间复杂度O(1)，执行发现超时。。

    ```
    class Solution:
        def maxArea(self, height: List[int]) -> int:
            ans = 0
            for i in range(len(height)-1):
                for j in range(len(height)):
                    temp = min(height[i], height[j])*(j-i)
                    ans = max(ans, temp)
            return ans
    ```

- 反馈（cn leetcode -> com leetcode）：

  - 双指针法（背+理解+写）：  时间复杂度O(n)，空间复杂度O(1)  

    ```
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
    ```

    

  - 国际站看排名前几个的内容没有新的思路，完成

# move zero(> 3 times) ——作业题

题目链接：https://leetcode-cn.com/problems/move-zeroes/

## 四步切题法：

- 先看题目，输入数组，输出数组（调整所有0到末尾，保持非0的顺序不变）

  - 限制条件：不能额外拷贝数组，尽量减少操作次数

- 想法：

  - 解法一，统计0的数量，最后删除+补上   时间复杂度最差是O(n^2)，空间复杂度是O(1)

- 代码：

  ```
          n = nums.count(0)
          if n == len(nums):
              return nums
          for i in range(n):
              nums.append(0)
              nums.remove(0)
          return nums
  ```

- 测试通过

## 五毒神掌：

看leetcode的解法，记

- 社区解法二，双指针。   时间复杂度是O(n)，空间复杂度是O(1)

  ```
  # 社区解法二，两个指针，增到非零就互换
          j = 0
          for i in range(len(nums)):
              if nums[i] != 0:
                  nums[i],nums[j]=nums[j],nums[i]
                  j+=1
          return nums
  ```
- 社区解法三，双变量，非零元素替换0，然后非0元素置0
  ```
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0
                j+=1
        return nums

  ```

- 国际区解法，前几个python3的没看到新的思路



# two sum（>5 times）  _   作业题

题目链接： https://leetcode-cn.com/problems/two-sum/ 

**四步切题法**

## 0、先看题目

**输入** 一个整数数组 nums 和一个目标值 target

**输出** 和为目标值的两个整数，返回他们的数组下标

假设每种输入只对应一个答案，且数组中同一个元素不能使用两遍（这里不能使用两遍是什么意思？）

**初步看没有什么坑**

## 1、初始想法

- 暴力解法循环
  - i，j 两个下标循环（i在0,n-1，j在i+1,n），如果两个下标对应的值为 target，则返回两个下标构成的数组，否则返回[]
- 选择一个num1，判断num2 = target - num1在剩余数组中是否存在

## 2、代码实现

- 暴力解法  O(n^2)

  ```
  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
          length = len(nums)
          for i in range(0, length-1):
              for j in range(i+1, length):
                  if nums[i] + nums[j] == target:
                      return [i , j]
          return []
  ```

- 判断num2是否在数组中存在 O(n)

  ```
  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
          length = len(nums)
          for i in range(0 , length-1):
              num2 = target - nums[i]
              if num2 in nums[i+1:]:
                  return [i, nums.index(num2)]
              else:
                  continue
          return []
          
          
  再简化版的代码：
  
  def twoSum(self, nums, target):
          for i in range(len(nums)):
              if target-nums[i] in nums[i+1:]:
                  return [i,nums.index(target-nums[i],i+1)]
  ```

  执行后碰到[3,3] 6这样的用例过不去，问题出在nums.index(num2)返回了第一个同样值的index，想了五分钟没想到方法，直接看题解

  最后受到leetcode上的代码启发，问题得到解决



## 3、别人的题解

- 用num2来判断 - 跟我初始的想法2一样

  ```
  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
          lens = len(nums)
          j=-1
          for i in range(lens):
              if (target - nums[i]) in nums:
                  if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):#如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
                    continue
                  else:
                      j = nums.index(target - nums[i],i+1) #index(x,i+1)是从num1后的序列后找num2                
                      break
          if j>0:
              return [i,j]
          else:
              return []
  ```

  - **受到这个代码的启发，将上述自己写的代码中  return [i, nums.index(num2)] 改为 return [i, nums.index(num2, i+1)]**

- 在num2方法的基础上，优化解法。 num2 的查找并不需要每次从 nums 查找一遍，只需要从 num1 位置之前或之后查找即可。但为了方便 index 这里选择从 num1 位置之前查找

  ```
  class Solution:
      def twoSum(self, nums, target):
          lens = len(nums)
          j=-1
          for i in range(1,lens):
              temp = nums[:i]
              if (target - nums[i]) in temp:
                  j = temp.index(target - nums[i])
                  break
          if j>=0:
              return [j,i]
  ```

- 在num2初始方法基础上，引入字典来模拟hash查询的过程，记录了num1、num2的值和位置，省去再查num2索引的步骤

  ```
  class Solution:
      def twoSum(self, nums, target):
          hashmap={}
          for ind,num in enumerate(nums):
              hashmap[num] = ind
          for i,num in enumerate(nums):
              j = hashmap.get(target - num)
              if j is not None and i!=j:
                  return [i,j]
  ```

- 在上面解法的基础上，再减少一次循环，将后面的查找放在前面的enumerate中进行即可

  ```
  class Solution:
      def twoSum(self, nums, target):
          hashmap={}
          for i,num in enumerate(nums):
              if hashmap.get(target - num) is not None:
                  return [i,hashmap.get(target - num)]
              hashmap[num] = i
  
  
  ```



再看看leetcode.com中大牛的写法

- 也是hash的方式 O(n)

```
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
```





## 最后的代码

O(n^2)  暴力

```
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```

O(n)  判断num2

```
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                return [i, nums.index(target - nums[i], i+1)]
        return []

```

O(n) 引入hash表，减少nums查询复杂度

```
class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i, n in enumerate(nums):
            if hashmap.get(target - n) is not None:
                return [i, hashmap.get(target - n)]
            hashmap[n] = i

```





# three sum(>5 times)

问题链接： https://leetcode-cn.com/problems/3sum/ 

## 初始思路

1、暴力，类似two sum的思路去解。 用到三层循环，且要加入去重判断

2、将nums[i]作为target，nums[j] nums[k]作为two sum的方式 去解，且要加入去重判断

3、将nums[i]作为target，将剩下的数组hash？ 加去重

4、无



## 写代码

1、暴力法，O(n^3)  超出时间限制

```python
class Solution:
    def threeSum(self, nums):
        result = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    # print("aa %i %i %i" %(nums[i],nums[j],nums[k]))
                    if nums[i] + nums[j] + nums[k] == 0:
                       temp = [nums[i], nums[j], nums[k]]
                       temp.sort()
                       if temp in result:
                          pass
                       else:
                          result.append(temp)
        if len(result) == 0:
            return []
        else:
            return result
```

2、3 初步想去重不好做，暂时没写

## 看题解

1、排序+双指针

优秀题解的思路如下：

- 本题难点在于如何去重

算法流程：

- 首先，特殊情况判断。 如果数组为null或者长度小于3，返回[]

- 对数组进行排序

- 遍历排序后的数组

  - 如果nums[i]>0，因为数组已经排序好，因此3数之和不可能=0，返回结果

  - 对于重复元素，跳过，避免出现重复解

  - 令左指针 L=i+1，右指针 R=n-1，当 L<R时，执行循环：

    - 当 nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R移到下一位置，寻找新的解
    - 若和大于 0，说明 nums[R]太大，R 左移
    - 若和小于 0，说明 nums[L] 太小，L 右移

    



- 代码实现：

  - 时间复杂度 O(n logn)+O(n)*O(n)  = O(n^2)
  - 空间复杂度 O(1)

  ```
  class Solution:
      def threeSum(self, nums):
          # 优秀解法
          res = []
          n = len(nums)
          #判定特殊情况
          if not nums or len(nums)<3:
              return []
          nums.sort()
          for i in range(n):
              if nums[i] > 0:
                  return res
              if i > 0 and nums[i]==nums[i-1]:
                  continue
              L = i+1
              R = n-1
              while L<R:
                  if nums[i]+nums[L]+nums[R]==0:
                      res.append([nums[i],nums[L],nums[R]])
                      while L<R and nums[L]==nums[L+1]:
                          L = L+1
                      while L<R and nums[R]==nums[R-1]:
                          R = R-1
                      L = L+1
                      R = R-1
                  elif nums[i]+nums[L]+nums[R]<0:
                      L = L+1
                  else:
                      R = R-1
          return res
  ```

- leetcode好句记录：**犹豫不决先排序，步步逼近双指针** 



今天在国际站中看到了一个新思路，效率比较高，记录下来

- 基本思路是利用set去重，然后区分三数和为0的情况为四种  3个0， 1个0，1+ 1-，2- 1+，1- 2+。

  ```
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
  ```

  
