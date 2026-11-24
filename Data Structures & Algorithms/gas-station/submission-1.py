class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        max_gas = float('-inf')
        for i in range(len(gas)):
            if gas[i] > max_gas:
                max_gas = gas[i]
                index = i

        for i in range(index+1, len(gas)-1):
            max_gas -= cost[i]
            max_gas += gas[i]

        for j in range(index):
            if j == 0:
                max_gas -= cost[-1]
            else: max_gas -= cost[j-1]
            max_gas += gas[j]

        if max_gas > cost[index-1]: return index
        else:
            return -1
