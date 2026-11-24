class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        temp = sorted(stones)
        temp = temp[::-1]
        queue = collections.deque(temp)
        while len(queue) > 1:
            firstnum = queue.popleft()
            secondnum = queue.popleft()
            dif = abs(firstnum - secondnum)
            queue.append(dif)
            temp = list(queue)
            temp.sort()
            temp = temp[::-1]
            queue = collections.deque(temp)
        return queue.popleft()