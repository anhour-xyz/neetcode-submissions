class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets.sort(key = lambda x:x[0])
        i = 0
        l, r = 0, len(triplets) - 1
        while l < r:
            left = triplets[l]
            right = triplets[r]
            if max(left[i],right[i]) < target[i]:
                return False
            elif max(left[i],right[i]) == target[i]:
                i += 1
                while i < len(target) and max(left[i],right[i]) == target[i]:
                    i += 1
                if i == len(target): return True
                else: 
                    i = 0
                    r -= 1
            else:
                r -= 1
        return False
            