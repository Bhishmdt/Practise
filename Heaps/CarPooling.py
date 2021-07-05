"""
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)
Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.
The locations are given as the number of kilometers due east from your vehicle's initial location.
Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.
"""
import heapq

def carPooling(trips, capacity):
    # Min-Heapify by start_location
    trips = [(e[1], e[0], e[2]) for e in trips]
    heapq.heapify(trips)
    vehicle = []
    for i in range(len(trips)):
        start_location, num_passengers, end_location = heapq.heappop(trips)
        while len(vehicle) > 0:
            # Remove passengers from vehicle if end_location of passenger in vehicle is less than or equal to start_location
            end_location_p, num_passengers_p = heapq.heappop(vehicle)
            capacity += num_passengers_p
            if end_location_p > start_location:
                heapq.heappush(vehicle, (end_location_p, num_passengers_p))
                capacity -= num_passengers_p
                break
        # Push new passenger into the vehicle
        heapq.heappush(vehicle, (end_location, num_passengers))
        capacity -= num_passengers
        if capacity < 0:
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

    trips = [[2, 1, 5], [3, 5, 7]]
    capacity = 3
    print(carPooling(trips, capacity))
    # Returns True