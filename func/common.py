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