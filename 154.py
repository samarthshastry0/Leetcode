class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, r = 0,n-1

        while l < r :
            m = l + (r-l)//2

            if nums[m] > nums[r] :
                l = m+1
            elif nums[m] < nums[l] :
                r = m
            else :
                r -= 1
                
        return nums[l]