class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        scanned = set()
        t = 0
        i = 0

        while t < len(nums):
            if nums[t] not in scanned:
                scanned.add(nums[t])
            else:
                i = t + 1
                while i <len(nums) and nums[i] in scanned:
                    i += 1
                if i < len(nums):
                    scanned.add(nums[i])
                    nums[t], nums[i] = nums[i], nums[t]
                else:
                    break
            t += 1
        return len(scanned)