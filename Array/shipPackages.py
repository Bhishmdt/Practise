"""
A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the
conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
"""

def shipWithinDays(weights, days):
    # Minimum and maximum required capacity
    min_required, max_required = max(weights), sum(weights)
    # Binary search for right capacity
    while min_required < max_required:
        mid = (min_required + max_required) // 2
        days_needed = 1
        cargo = 0
        for w in weights:
            if w + cargo > mid:
                days_needed += 1
                cargo = 0
            cargo += w
        if days_needed > days:
            min_required = mid + 1
        else:
            max_required = mid
    return min_required

if __name__ == '__main__':
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5
    print(shipWithinDays(weights, days))
    # Returns 15

    weights = [3, 2, 2, 4, 1, 4]
    days = 3
    print(shipWithinDays(weights, days))
    # Returns 6