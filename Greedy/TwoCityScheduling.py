"""
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti],
the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
"""


def twoCitySchedCost(costs):
    # Send all to A
    costA = [a for a, b in costs]
    # Send to B if diff of cost is min
    diff = [b - a for a, b in costs]

    diff.sort()

    return sum(costA) + sum(diff[:len(costs) // 2])

if __name__ == '__main__':
    costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
    print(twoCitySchedCost(costs))
    # Returns 1859

    costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
    print(twoCitySchedCost(costs))
    # Returns 110