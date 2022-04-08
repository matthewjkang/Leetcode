class Solution:
    def myAtoi(self,s):
        res = ""
        nums = ['0','1','2','3','4','5','6','7','8','9']
        op = ["-","+"]
        hasNums = False
        opCount = 0
        for i in s:
            if i == " ":
                continue
            if i == '-' or i == "+":
                if opCount > 0:
                    break
                if opCount == 0:
                    res+=i
                    opCount += 1
            if i in nums:
                res+=i
                hasNums = True
                opCount = 1
            if i not in nums and i not in op:
                break
        
        if hasNums == False:
            return 0
        if int(res) <= -2**31:
            return -2**31
        if int(res) >= 2**31 - 1:
            return 2**31 - 1
        else:
            return int(res)
            