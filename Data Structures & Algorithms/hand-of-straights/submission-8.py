class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        map = defaultdict(int)
        for h in hand:
            map[h] += 1
        minVal = min(hand)
        k = len(hand) // groupSize
        for _ in range(k):
            minVal = min(map.keys())
            if minVal not in map: return False
            map[minVal] -= 1
            if map[minVal] == 0: del map[minVal]
            cur = minVal
            for _ in range(groupSize-1):
                if cur + 1 not in map: return False
                map[cur+1] -= 1
                if map[cur+1] == 0: del map[cur+1]
                cur += 1
            

        return True


        