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
        visit = {None:None}
        visit[node] = Node(node.val)
        q = deque()
        q.append(node)
        while q:
            for _ in range(len(q)):
                n = q.popleft()
                for nei in n.neighbors:
                    if nei not in visit:
                        q.append(nei)
                        visit[nei] = Node(nei.val)
                    visit[n].neighbors.append(visit[nei])
        return visit[node]