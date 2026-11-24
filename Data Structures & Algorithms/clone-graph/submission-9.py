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
        q = deque()
        q.append(node)
        visit[node] = Node(node.val)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in node.neighbors:
                    if nei not in visit:
                        visit[nei] = Node(nei.val)
                        q.append(nei)
                    visit[node].neighbors.append(visit[nei])
        return visit[node]
                    
