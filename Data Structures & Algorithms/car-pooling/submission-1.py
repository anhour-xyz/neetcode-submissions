class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        overlap = [trips[0]]
        for i in range(1,len(trips)):
            n,s,e = trips[i]
            if s < overlap[-1][2]:
                total = overlap[-1][0] + n
                if total > capacity: return False
                else:
                    overlap[-1][0] = total
                    overlap[-1][2] = max(overlap[-1][2], e)
            else:
                total = n
                if n > capacity: return False
                else:
                    overlap.append(trips[i])
        return True

