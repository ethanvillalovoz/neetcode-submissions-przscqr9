class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for i in range(len(arr)):
            max_value = -1
            for j in range(i+1, len(arr)):
                max_value = max(max_value, arr[j])

            arr[i] = max_value

        arr[-1] = -1
        
        return arr