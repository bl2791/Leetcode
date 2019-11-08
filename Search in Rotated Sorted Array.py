class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            else:
                if nums[mid] >= nums[left]:
                    if target < nums[mid] and target >= nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if target >= nums[mid] and target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1               
        return -1