"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        q = deque()
        q.append(node)
        visit = {}
        visit[node] = Node(node.val)

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                for i in cur.neighbors:
                    if i not in visit:
                        visit[i] = Node(i.val)
                        q.append(i)
                    visit[cur].neighbors.append(visit[i])

        return visit[node]