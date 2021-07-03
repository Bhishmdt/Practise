"""
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)
Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.
The locations are given as the number of kilometers due east from your vehicle's initial location.
Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.
"""


def carPooling(trips, capacity):
    l = []
    for trip in trips:
        # Append start, num_passengers
        l.append((trip[1], trip[0]))
        # Append end, num_passengers
        l.append((trip[2], -trip[0]))

    l.sort()
    passengers = 0
    for p in l:
        passengers += p[1]
        if passengers > capacity:
            return False
    return True

if __name__ == '__main__':
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4
    print(carPooling(trips, capacity))
    # Returns False

    trips = [[3, 2, 7], [3, 7, 9], [8, 3, 9]]
    capacity = 11
    print(carPooling(trips, capacity))
    # Returns True