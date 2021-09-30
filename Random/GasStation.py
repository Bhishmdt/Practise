"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
"""


def canCompleteCircuit(gas, cost) -> int:
    start_station = -1
    curr_reserve = -1
    full_reserve = 0
    for i in range(len(gas)):
        full_reserve += gas[i] - cost[i]
        if gas[i] - cost[i] >= 0 and curr_reserve < 0:
            curr_reserve = gas[i] - cost[i]
            start_station = i
        # if gas[i] - cost[i] >= 0 and curr_reserve >= 0:
        #     curr_reserve += gas[i] - cost[i]
        # if gas[i] - cost[i] < 0 and curr_reserve + gas[i] - cost[i] < 0:
        #     curr_reserve = -1
        # if gas[i] - cost[i] < 0 and curr_reserve + gas[i] - cost[i] >= 0:
        #     curr_reserve += gas[i] - cost[i]
        else:
            curr_reserve += gas[i] - cost[i]
    if full_reserve >= 0:
        return start_station
    else:
        return -1

if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(canCompleteCircuit(gas, cost))
    # Returns 3

    gas = [2, 3, 4]
    cost = [3, 4, 3]
    print(canCompleteCircuit(gas, cost))
    # Returns -1