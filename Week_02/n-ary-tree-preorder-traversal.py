#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # third: leetcode.com most vote answer
        res, q = [], root and [root]
        while q:
            node = q.pop()
            res.append(node.val)
            q+=[child for child in node.children[::-1] if child]  #优雅的实现
        return res

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


        # # first recursion
        # if not root: return []
        # res = [root.val]
        # for i in root.children:
        #     res += self.preorder(i)
        # return res

# @lc code=end

