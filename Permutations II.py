class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def DFS(result, permutation, nums):
            if len(nums) == 1:
                result.append(permutation + [nums[0]])
            else:
                a = None
                for i in range(len(nums)):
                    if nums[i] != a:
                        a = nums[i]
                        DFS(result, permutation + [nums[i]], nums[:i] + nums[i+1:])
                    else:
                        continue

        if len(nums) == 0:
            return nums
        nums = sorted(nums)
        result = []
        permutation = []
        DFS(result, permutation, nums)
        return result