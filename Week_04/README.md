使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
说明：同学们可以将自己的思路、代码写在第 4 周的学习总结中



- 思路：

  - 目标寻找半有序数组中中间无序的地方，我理解为求开头升序数组中第一个降序的地方，以示例为例，就是0所在的下标，index为4

  - 思路：

    - 暴力：遍历数组，找到一个中间数字符合这个条件，时间复杂度O(n)，空间复杂度O(1)

      ```
      if not nums: return -1
      n = len(nums)
      # exclude index 0
      for i in range(1, n):
      	if nums[i] < nums[i-1]:
      		return i	 
      ```

    - 类似二分思想，找到一个值，值小于左边的数，且小于右边的数，即找极小值(没有详细调试，应该是有bug的)

      ```
      if not nums: return -1
      n = len(nums)
      l = 0
      r = n-1
      while l < r:
      	mid = l + (r - l)//2
      	if nums[mid] > nums[n-1]:
      		l = mid+1
      	elif nums[mid] < nums[n-1]:
      		r = mid
      return mid
      		
      ```

      