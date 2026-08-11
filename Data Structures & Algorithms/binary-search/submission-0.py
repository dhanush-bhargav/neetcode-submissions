class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            item = nums[mid]
            if target == item:
                return mid
            elif target < item:
                right = mid - 1
            elif target > item:
                left = mid + 1
        return -1