class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        if nums[left] <= target <= nums[-1]:
            search_left = left
            search_right = len(nums) - 1
        elif nums[0] <= target <= nums[left-1]:
            search_left = 0
            search_right = left - 1
        else:
            return -1

        print(search_left)
        print(search_right)

        while search_left <= search_right:
            mid = (search_left + search_right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                search_right = mid - 1
            elif target > nums[mid]:
                search_left = mid + 1
        
        return -1
