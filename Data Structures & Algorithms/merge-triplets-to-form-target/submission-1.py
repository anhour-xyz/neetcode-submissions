class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        max_1 = float('-inf')
        max_2 = float('-inf')
        max_3 = float('-inf')
        for i in range(len(triplets)-1):
            for j in range(i+1,len(triplets)):
                first = triplets[i-1]
                second = triplets[i]
                max_1 = max(first[0],second[0])
                max_2 = max(first[1],second[1])
                max_3 = max(first[2],second[2])
                if max_1 == target[0] and max_2 == target[1] and max_3 == target[2]:
                    return True
        return False
