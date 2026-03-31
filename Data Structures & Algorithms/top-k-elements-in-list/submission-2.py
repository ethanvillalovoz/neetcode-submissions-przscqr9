class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # first I can count the frequency of how many times via a dictionary
        counter = {}

        for num in nums:

            counter[num] = 1 + counter.get(num, 0)

        # now I want to do like a bucket sorting trick where I will use the 
        # index to determine the freq of the number

        freq = [[] for i in range(len(nums) + 1)]

        for num, count in counter.items():

            freq[count].append(num)

        # now I will go through the freq list in reverse and go through each 
        # bucket

        res = []

        for i in range(len(freq)-1, 0 , -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res