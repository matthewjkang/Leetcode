import math
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        combined = sorted(nums1+nums2)
        is_odd = len(combined) % 2 != 0
        if is_odd:
            medianIndex = math.ceil(len(combined)/2) - 1
            return combined[medianIndex]
        else:
            medianIndex = round(len(combined) / 2)
            return (combined[medianIndex]+combined[medianIndex-1])/2

print(Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
