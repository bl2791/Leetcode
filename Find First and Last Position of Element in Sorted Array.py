# Solution 1
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        left = 0
        right = len(nums) - 1
        start = -1
        end = -1
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                idx1 = mid
                idx2 = mid
                while idx1 >= 0 and nums[idx1] == target:
                    idx1 -= 1
                start = idx1 + 1
                while idx2 < len(nums) and nums[idx2] == target:
                    idx2 += 1
                end = idx2 - 1
                break
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return [start, end]


# Solution 2
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        def first(nums, target, low, high, mid):
            if low <= high:
                if target == nums[mid]:
                    if mid == 0 or nums[mid] > nums[mid - 1]:
                        return mid
                    high = mid - 1
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                mid = (low + high) // 2
                return first(nums, target, low, high, mid)
            else:
                return -1
                
        def last(nums, target, low, high, mid):
            if low <= high:
                if target == nums[mid]:
                    if mid == len(nums) - 1 or nums[mid] < nums[mid + 1]:
                        return mid
                    low = mid + 1
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                mid = (low + high) // 2
                return last(nums, target, low, high, mid)
            else:
                return -1
        
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        return(first(nums, target, low, high, mid), last(nums, target, low, high, mid))    