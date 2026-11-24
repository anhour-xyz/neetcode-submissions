class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        map = defaultdict(int)
        for h in hand:
            map[h] += 1
        res = []
        for key, value in map.items():
            while map[key] > 0:
                map[key] -= 1
                cur = key
                temp = [cur]
                length = 1
                while cur + 1 in map and map[cur+1] > 0 and length < groupSize:
                    map[cur+1] -= 1
                    cur = cur + 1
                    temp.append(cur)
                    length += 1
                res.append(temp)

        for r in res:
            if len(r) != groupSize: return False
        return True


        
        