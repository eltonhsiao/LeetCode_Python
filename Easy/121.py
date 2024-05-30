from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxValue = 0
        currentValue = 0
        buy = prices[0]

        for i in prices[1:]:
            if i > buy:
                currentValue = i - buy
                if currentValue > maxValue:
                    maxValue = currentValue
            else:
                buy = i

        return maxValue

def main():
    try:
        output = Solution.maxProfit("",[7,1,5,3,6,4])
        print(output)
    except ValueError as ve:
        return str(ve)

if __name__ == "__main__":
    main()