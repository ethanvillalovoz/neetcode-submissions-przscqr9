class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        replace = -1

        for i in range(len(arr)-1, -1, -1):
            if replace < arr[i]:
                arr[i], replace = replace, arr[i]
            else:
                arr[i] = replace

        return arr