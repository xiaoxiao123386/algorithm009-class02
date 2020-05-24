#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 第二种解法，递归 待补充（发现写错问题了）
        

        第一种解法，引入新结点
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
# @lc code=end

