from typing import List
import operator

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        
        tank = [x - y for x, y in zip(gas, cost)]
        #tank = list(map(operator.sub, gas, cost))
        print(tank)
        suply = 0
        j = 0
        for i in range(len(tank)):
            suply += tank[i]
            if suply < 0:
                suply = 0
                j = i + 1

        return j


def main():
    try:
        output = Solution.canCompleteCircuit("",[2,3,4],[3,4,3])
        print(output)
    except ValueError as ve:
        return str(ve)

if __name__ == "__main__":
    main()