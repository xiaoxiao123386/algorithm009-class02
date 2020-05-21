学习笔记



# two sum

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





# three sum

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