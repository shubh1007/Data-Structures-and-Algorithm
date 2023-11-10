class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums1.sort()
        nums2.sort()
        i = j = 0
        output = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                output.append(nums1[i])
                i += 1
                j += 1
        return output 
        