class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map = {'b':1,'a':1,'l':2,'o':12,'n':1}
        check = defaultdict(int)
        for i in text:
            if i in map:
                check[i] += 1
        res = float('inf')
        for key, value in check.items():
            if key == "l" or key == "o":
                res = min(res, value // 2)
            else:
                res = min(res,value)
        return res if res != float('inf') else 0
            