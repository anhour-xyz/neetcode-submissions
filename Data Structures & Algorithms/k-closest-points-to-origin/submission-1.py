class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dis = defaultdict(list)
        for i in range(len(points)):
            temp = (abs(points[i][0])**2 + abs(points[i][1])**2)**0.5
            dis[temp].append(i)

        all_keys = []
        for key in dis.keys():
            all_keys.append(key)
        all_keys.sort()
        find = set()

        j = 0
        while k > 0:
            k -= len(dis[all_keys[j]])
            find.add(all_keys[j])
            j += 1

        res = []

        for key,value in dis.items():
            if key in find:
                for v in value:
                    res.append(points[v])
        return res
        

