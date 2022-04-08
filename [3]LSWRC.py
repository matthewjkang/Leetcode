'''
Input: s = "abcabcbb"
Output: 3
Input: s = "bbbbb"
Output: 1
Input: s = "pwwkew"
Output: 3
'''
class Solution:
    def lengthOfLongestSubstring(self, s): 
        substring = []
        longest = 0
        for char in s:
            if char not in substring:
                substring.append(char)
                if len(substring) > longest:
                    longest = len(substring)
            else:
                repeat_index = substring.index(char)
                substring = substring[repeat_index+1:]
                substring.append(char)
        return longest
            
print(Solution().lengthOfLongestSubstring(s = "bbbbb"))