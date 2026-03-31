class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_value = -1
        ans = [0] * len(arr)

        for i in range(len(arr) -1, -1, -1):
            ans[i] = max_value
            max_value = max(max_value, arr[i])

        return ans