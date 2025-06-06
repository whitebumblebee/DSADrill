"""
My solution without kadane's algo. Passes 201 out of 210 test cases. Only failing with TLE.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = -1000000
        aggr = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i] > sum_:
                sum_ = nums[i]
            aggr += nums[i]
            for j in range(i+1, len(nums)):
                aggr += nums[j]
                if aggr > sum_:
                    sum_ = aggr
            aggr = 0
        return sum_
    

"""
Solution with Kadane's algorithm
"""