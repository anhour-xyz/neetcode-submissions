class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0,0,0]
        for i in range(1,len(triplets)):
            x2,y2,z2 = triplets[i][0], triplets[i][1], triplets[i][2]
            x1,y1,z1 = triplets[i-1][0], triplets[i-1][1], triplets[i-1][2]
            if max(x1,x2) <= target[0] and max(y1,y2) <= target[1] and max(z1,z2) <= target[2]:
                res[0] = max(x1,x2)
                res[1] = max(y1,y2)
                res[2] = max(z1,z2)
        return res == target



