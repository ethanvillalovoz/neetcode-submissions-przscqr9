class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) == 0:
            return 0

        output = 0
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]

        for i in range(1, n):
            leftMax[i] = max(height[i], leftMax[i-1])

        rightMax[n-1] = height[n-1]

        for i in range(n-2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i+1])

        print(rightMax)
        print(leftMax)
        for i in range(len(rightMax)):
            print(output)
            print(rightMax[i], leftMax[i], height[i])
            output += min(rightMax[i], leftMax[i]) - height[i]

        return output