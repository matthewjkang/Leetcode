"""
word = bbabab

word[left=1:right=2] = b
    are the letters to the left and right the same?
        no [bba]
            left += 1
            right += 1

word[left =2:right =3] = a
    is s[ left-1] = s[right]
        yes [bab]
            left -= 1
            right += 1

word[left = 1:right=4] = bab
    is s[left-1] = s[right]
        no ( s[0] = b, s[4] = a )
            left -=1
            right +=1

word[left = 0:right=5] = b bab a
    if left-1 not in range(len(s)):
        left += 1
        right += 1

word[left=1:right=6]

"""

word = s = "asdffdsa"
class Solution(object):

    def longestPalindrome(self, s):
        left = 1
        right = 2
        palindrome = "test"

        while right < len(s): 
            print(left,right,len(s)) #REMOVE
            if left-1 < 0 : 
                left += 1
                right += 1
                print(left,right) #REMOVE

            elif s[left-1] == s[right]: 
                left -= 1
                right += 1
                if len(s[left:right]) > len(palindrome):
                    palindrome = s[left:right]
            else:
                left += 1 
                right += 1 
        return palindrome
        

sol = Solution().longestPalindrome(word)
print(sol)