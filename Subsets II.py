class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def subsets(result, lst, nums):
            result.append(lst)
            if len(nums) == 1:
                result.append(lst + [nums[0]])
            else: 
                for i in range(len(nums)):
                    if i > 0:
                        if nums[i] == nums[i - 1]:
                            continue
                    subsets(result, lst + [nums[i]], nums[i + 1 :])
        nums = sorted(nums)
        result = []
        lst = []
        subsets(result, lst, nums)
        return result