class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        map = defaultdict(int)
        for c in chars:
            map[c] += 1
        res = 0
        for word in words:
            if len(word) > len(chars): continue
            check = True
            temp = map.copy()
            for i in word:
                if i not in temp or temp[i] == 0:
                    check = False
                    break
                else:
                    temp[i] -= 1
            if check == True: res += len(word)
        return res

