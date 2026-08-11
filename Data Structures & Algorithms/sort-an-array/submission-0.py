class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        mid = len(nums) // 2
        left = 0
        right = len(nums)
        left_sorted = self.sortArray(nums[left:mid])
        right_sorted = self.sortArray(nums[mid:right])

        result = [0] * len(nums)
        i=j=k=0

        while(i<len(left_sorted) and j<len(right_sorted)):
            if left_sorted[i] <= right_sorted[j]:
                result[k] = left_sorted[i]
                i += 1
            else:
                result[k] = right_sorted[j]
                j += 1
            k += 1
        
        while i<len(left_sorted):
            result[k] = left_sorted[i]
            k +=1
            i +=1

        while j<len(right_sorted):
            result[k] = right_sorted[j]
            k +=1
            j +=1
        
        return result