"""
Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event at any time d.
Return the maximum number of events you can attend.
"""

import heapq

def maxEvents(events):
    events.sort()
    heap = []
    result = 0
    start = 0
    while heap or events:
        if not heap:
            start = events[0][0]
        while events and events[0][0] <= start:
            heapq.heappush(heap, events.pop(0)[1])
        heapq.heappop(heap)
        result += 1
        start += 1
        while heap and heap[0] < start:
            heapq.heappop(heap)
    return result

if __name__ == '__main__':
    events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
    print(maxEvents(events))
    # Returns 4

    events = [[52, 79], [7, 34]]
    print(maxEvents(events))
    # Returns 2