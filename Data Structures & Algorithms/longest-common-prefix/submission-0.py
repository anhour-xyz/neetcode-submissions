class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = float('inf')
        for s in strs:
            if len(s) < shortest:
                shortest = len(s)
                shortest_word = s
        shortest_word = list(shortest_word)

        for s in strs:
            idx = len(shortest_word) - 1
            for i in range(idx+1):
                if s[i] != shortest_word[i]:
                    shortest_word = shortest_word[:i]
                    break
        return ''.join(shortest_word)


        