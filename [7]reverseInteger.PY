class Solution:
    def reverse(self, x: int) -> int:
        
        if x >= 0:
            temp = int(str(x)[::-1])
            if temp < ((2**31)-1):
                return temp
            else:
                return 0
        
        if x < 0:
            temp2 = "-"+str(x)[::-1]
            temp3 = int(temp2[:len(temp2)-1])
            if temp3 > (-2**31):
                return temp3
            else:
                return 0

