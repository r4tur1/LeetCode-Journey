class Solution(object):
    def twoSum(self, nums, target):
        result_sum=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                result_sum = nums[i] + nums[j]
                if result_sum == target:
                    return [i, j]

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        