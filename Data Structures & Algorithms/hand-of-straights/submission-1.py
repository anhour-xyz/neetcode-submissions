class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        map = defaultdict(int)
        for h in hand:
            map[h] += 1
        
        res = []
        for key, value in map.items():
            while map[key] != 0:
                map[key] -= 1
                cur = key
                length = 1
                temp = [cur]
                while cur + 1 in map and map[cur+1] != 0 and length < groupSize:
                    length += 1
                    cur = cur + 1
                    temp.append(cur)
                    map[cur] -= 1
                res.append(temp)
                value -= 1

        for r in res:
            if len(r) != groupSize: return False
        return True
                
        