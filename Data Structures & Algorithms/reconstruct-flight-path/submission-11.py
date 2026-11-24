class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        map = defaultdict(list)
        for start,end in sorted(tickets,reverse = True):
            map[start].append(end)
        res = []
        def dfs(src):
            while map[src]:
                dst = map[src].pop()
                dfs(dst)
            res.append(src)

        dfs("JFK")
        return res[::-1]