class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.postMap = defaultdict(list)
        self.cnt = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append([self.cnt,tweetId])
        self.cnt -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.postMap:
                idx = len(self.postMap[followeeId]) - 1
                cnt, tweetId = self.postMap[followeeId][idx]
                heapq.heappush(minHeap,[cnt,tweetId,followeeId,idx-1])
        while minHeap and len(res) < 10:
            cnt, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                cnt, tweetId = self.postMap[followeeId][idx]
                heapq.heappush(minHeap,[cnt,tweetId,followeeId,idx-1])
        return res        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        return None
