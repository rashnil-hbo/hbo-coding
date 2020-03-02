import heapq


def getMeetingRooms(intervals):
    intervals.sort(key = lambda x: x[0])
    heap = []
    for interval in intervals:
        if heap and interval[0]>= heap[0]:
            heapq.heapreplace(heap, interval[1])
        else:
            heapq.heappush(heap, interval[1])
    return len(heap)


assert(getMeetingRooms([])) == 0
assert(getMeetingRooms([(0,10), (10,20), (5,10)])) == 2
assert(getMeetingRooms([(20,30), (10,21), (5,50)])) == 3
assert(getMeetingRooms([(0,20), (10,23), (12,23), (12,23), (22,30)])) == 4
assert(getMeetingRooms([(0, 10), (10, 20), (15, 30), (15, 30), (30, 40), (35, 50), (40, 45)])) == 3