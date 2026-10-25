class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            difference = gas[i] - cost[i]
            total += difference
            tank += difference

            if tank < 0:
                start = i + 1
                tank = 0

        return start if total >= 0 else -1
