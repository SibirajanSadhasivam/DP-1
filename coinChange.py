# Time complexity -> O(N)
# Space complexity -> O(1)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        
        
        for i in range(1,amount+1):
            for j in coins:
                if j <= i:
                    dp[i] = min(dp[i], dp[i-j]+1)
                    
        if dp[amount] == amount+1:
            return -1
        return dp[amount]