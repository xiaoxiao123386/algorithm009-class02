#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 第三种解法：妖魔化的双指针，比较不好理解，但可以做为一个思路
        if head == None:
            return None
        cur = head
        while head.next:
            tmp = head.next.next  # 存下一步该指向的节点
            head.next.next = cur  # 新链表的对应关系确定
            cur = head.next       # 不断右移指针
            head.next = tmp       # 移动head.next到下一个位置

        return cur

        # 第二种解法，递归实现
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead


        # 第一种解法，双指针迭代法，不断推进两个指针
        # cur = None
        # pre = head
        # while pre:
        #     tmp = pre.next
        #     pre.next = cur 
        #     cur = pre
        #     pre = tmp
        # return cur
        # @lc code=end

