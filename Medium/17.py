from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numDict = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}
        
        output = []
        def combinationHelpers(digits_rest, word):
            if len(digits_rest) == 0:
                output.append(word)
                return
            
            for letter in numDict[digits_rest[0]]:
                combinationHelpers(digits_rest[1:], word+letter)
        
        if digits:
            combinationHelpers(digits, "")

        return output

if __name__ == "__main__":
    output = Solution.letterCombinations(0, "23")
    print(output)