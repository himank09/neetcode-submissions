class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + [x for x in nums if x> 0] + [1]
        n = len(balloons)
        dp = [[0] * n for _ in range(n)]

        for length in range(1,n-1):
            for left in range(1,n- length):
                right = left + length -1 
                for k in range(left, right + 1):
                    coins = balloons[left -1] * balloons[k] * balloons[right + 1]
                    total = coins + dp[left][k-1] + dp[k + 1][right]
                    if total > dp[left][right]:
                        dp[left][right] = total

        return dp[1][n-2]            