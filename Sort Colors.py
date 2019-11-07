class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) != 0 :
            pointer1 = 0
            pointer2 = len(nums) - 1
            pointer3 = 0
        while pointer1 <= pointer2:
            if nums[pointer1] == 2:
                nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
                pointer2 -= 1
            elif nums[pointer1] == 0:
                nums[pointer1], nums[pointer3] = nums[pointer3], nums[pointer1]
                pointer3 += 1
                pointer1 += 1
            else:
                pointer1 += 1
        return nums