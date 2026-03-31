class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        lst = nums1 + nums2
        lst.sort()
        print(lst)

        if len(lst) % 2 == 0:
            return (lst[len(lst)// 2] + lst[(len(lst)// 2)-1]) / 2
        else:
            return lst[(len(lst)// 2)]