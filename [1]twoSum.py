class Solution:
    #nums = [2,7,11,15]
    #target = 9
    def twoSum(self,nums,target):
        empdict = {}
        for index,number in enumerate(nums): # (0, 2), (1, 7), (2, 11), (3, 15)
            h = target-number
            # 9-2 = 7
            # 9-7 = 2
            # 9-11 = -4
            # 9-15 = -6
            if number not in empdict:
                empdict[h] = index
            # if 2 not in empdict, empdict[7] = 0
            # if 7 not in empdict, empdict[2] = 1
            # if -4 not in empdict, empdict[-4] = 2
            else:
                return index,empdict[number]
