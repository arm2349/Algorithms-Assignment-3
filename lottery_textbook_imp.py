from sys import stdin
from collections import namedtuple
Event = namedtuple('Event', ['coordinate', 'type', 'index'])

def points_cover(starts, ends, points):
    count = [None] * len(points)

    events = []

    for i in range(len(starts)):
        events.append(Event(starts[i], 'l', i))
        events.append(Event(ends[i], 'r', i))
    for i in range (len(points)):
        events.append(Event(points[i], 'p', i))

    events = sorted(events)
    num_of_segs= 0
    for e in events:
        if e.type == 'l':
            num_of_segs +=1
        elif e.type == 'r':
            num_of_segs -=1
        elif e.type == 'p':
            count[e.index] = num_of_segs
        else:
            assert False
    return count

if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n,m = data[0], data[1]
    starts, ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    count = points_cover(starts, ends, points)
    print (*count)
