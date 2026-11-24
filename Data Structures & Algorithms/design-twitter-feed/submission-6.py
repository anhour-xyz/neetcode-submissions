class Twitter:

    def __init__(self):
        self.count = 0
        self.postMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.postMap:
                idx = len(self.postMap[followeeId]) - 1
                cnt, tweetId = self.postMap[followeeId][idx]
                minHeap.append([cnt,tweetId,followeeId,idx-1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            cnt,tweetId,followeeId,idx = heapq.heappop(minHeap)
            res.append(tweetId)
            while idx >= 0:
                cnt, tweetId = self.postMap[followeeId][idx]
                heapq.heappush([cnt,tweetId,followeeId,idx-1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

