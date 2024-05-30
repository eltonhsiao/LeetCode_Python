from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = {}

        def dp(coins: List[int], amount: int) -> int:
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if amount in table:
                return table[amount]
        
            min = float('inf')
            for coin in coins:
                val = dp(coins, amount-coin) + 1
                if min > val:
                    min = val
            table[amount] = min

            return min

        resp = dp(coins, amount)
        return -1 if resp == float('inf') else resp

    


if __name__ == "__main__":
    output = Solution.coinChange("", [2], 3)
    print(output)