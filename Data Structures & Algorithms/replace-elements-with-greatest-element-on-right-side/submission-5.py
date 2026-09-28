class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        largest = float("-inf")
        
        for i in range(len(arr) - 1, -1, -1):
            if largest < arr[i]:
                arr[i], largest = largest, arr[i]
            else:
                arr[i] = largest

        arr[-1] = -1

        return arr