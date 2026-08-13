class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        count = dict()

        for char in s:
            count[char] = 1 + count.get(char, 0)

        print(count)

        for char in t:
            
            if char in count and count[char] - 1 >= 0:
                count[char] -= 1
            else:
                return False

        return True