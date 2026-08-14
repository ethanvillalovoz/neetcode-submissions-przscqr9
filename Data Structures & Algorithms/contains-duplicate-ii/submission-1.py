class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # seen = defaultdict(int)

        # for i, num in enumerate(nums):
        #     if num in seen and abs(i - seen[num]) <= k:
        #         return True

        #     seen[num] = i

        # return False

        # Time: O(n)
        # Space: O(n)

        # sliding window approach

        seen = set()

        for i in range(len(nums)):

            if nums[i] in seen:
                return True

            seen.add(nums[i])

            if len(seen) > k:
                seen.remove(nums[i - k])

        return False



