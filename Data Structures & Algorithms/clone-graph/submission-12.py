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
        visit = {}
        q = deque()
        q.append(node)
        visit[node] = Node(node.val)
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                for nei in cur.neighbors:
                    if nei not in visit:
                        q.append(nei)
                        visit[nei] = Node(nei.val)

                    visit[cur].neighbors.append(visit[nei])
        return visit[node]