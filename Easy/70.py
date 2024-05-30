class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        dp = [0, 1, 2]
        for i in range(3, n + 1):
            dp.append(dp[i-1] + dp[i-2])
        
        return dp[n]
    

if __name__ == "__main__":
    output = Solution.climbStairs("", 3)
    print(output)