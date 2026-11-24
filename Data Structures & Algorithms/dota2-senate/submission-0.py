class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        map = {"D":0, "R":0}
        for c in senate:
            map[c] += 1
        q = deque(senate)
        target = None
        target_cnt = 0
        while q:
            if not map["R"]: return "Dire"
            if not map["D"]: return "Radiant"

            player = q.popleft()
            if player == target and target_cnt > 0:
                target_cnt -= 1
                map[player] -= 1
            else:
                target_cnt += 1
                target = "D" if player == "R" else "R"
                q.append(player)
        