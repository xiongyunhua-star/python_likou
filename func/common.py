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

import queue
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        initValue = image[sr][sc]
        if image[sr][sc] == color:
            return image
        directs = [[1,0],[-1,0],[0,1],[0,-1]] # 下 上 右  左
        x, y = len(image), len(image[0])
        image[sr][sc] = color
        q = queue.Queue()
        q.put([sr,sc])  # 放入队列
        while not q.empty():
            xi, yi = q.get()  #出队列
            for direct in directs:
                if 0 <= xi + direct[0] < x and 0 <= yi+direct[1]< y :
                    if image[xi+direct[0]][yi+direct[1]] == initValue:
                        q.put([xi+direct[0],yi+direct[1]])
                        image[xi+direct[0]][yi+direct[1]] = color
        return image