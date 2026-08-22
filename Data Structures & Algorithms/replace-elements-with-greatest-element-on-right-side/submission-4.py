class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max_value = arr[-1]
        
        for i in range(len(arr) - 1, -1, -1):
            if max_value < arr[i]:
                max_value, arr[i] = arr[i], max_value
            else:
                arr[i] = max_value


        arr[-1] = -1

        return arr