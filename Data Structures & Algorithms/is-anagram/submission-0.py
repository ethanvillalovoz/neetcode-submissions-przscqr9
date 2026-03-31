class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Base case - length
        if len(s) != len(t):
            return False

        # Create a counter for each letter occuring
        counter = {}

        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1

        for char in t:
            if char in counter and (counter[char] - 1 >= 0):
                counter[char] -= 1
            else:
                return False

        return True