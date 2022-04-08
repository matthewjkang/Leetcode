class Solution:
    def isValid(self, s):
        stack = list(s[0])
        symdict = { "(":")" , "{":"}" , "[":"]" }
        
        for char in s[1:]:
            if not stack:
                stack.insert(0,char)
                continue     
            stack.insert(0,char)
            if stack[1] in symdict and stack[0] == symdict[stack[1]]:
                stack.pop(0)
                stack.pop(0)

        return len(stack) == 0


