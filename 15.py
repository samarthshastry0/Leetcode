class Solution(object):
    def threeSum(self, nums):
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            

            left = i+1
            right = n - 1

            target = -nums[i]

            while left < right:
                s = nums[left] + nums[right]

                if s == target:
                    # Found a valid triplet
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif s < target:
                    left += 1
                else:
                    right -= 1

        return ans
