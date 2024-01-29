'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    	unique_sum = sum(set(nums))
    	return 2 * unique_sum - sum(nums)

