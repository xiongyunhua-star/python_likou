class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        pairs = {
            '{':'}',
            '[':']',
            '(':')'
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            else:  # ch == } ] )
                if stack and pairs[stack[-1]] == ch:
                    stack.pop()  #出栈
                elif stack and pairs[stack[-1]] != ch:
                    return False
                elif not stack:  #一次没入栈，就遇到}])
                    return False
        return not stack

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: [TreeNode]) -> list[int]:
        res = []
        def preorder(root: TreeNode):
            if root == None:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return res
