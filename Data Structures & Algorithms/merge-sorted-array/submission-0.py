class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        comp1 = m - 1
        comp2 = n - 1

        for i in range(m+n-1, -1, -1):
            if comp1< 0 or comp2<0:
                break
            if nums1[comp1] > nums2[comp2]:
                nums1[i], nums1[comp1] = nums1[comp1], nums1[i]
                comp1 -= 1
            else:
                nums1[i] = nums2[comp2]
                comp2 -= 1
            
        if comp1<0 and comp2 >= 0:
            while comp2 >= 0:
                nums1[comp2] = nums2[comp2]
                comp2 -= 1
        