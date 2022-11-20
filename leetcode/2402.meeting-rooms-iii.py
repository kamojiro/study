#
# @lc app=leetcode id=2402 lang=python3
#
# [2402] Meeting Rooms III
#

# @lc code=start
from heapq import heappop, heappush, heapify
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        held = [0]*n
        rooms = [i for i in range(n)]
        heapify(rooms)
        ending = []
        using = [False]*n
        for start, end in meetings:
            while ending and ending[0][0] <= start:
                _, end_room = heappop(ending)
                using[end_room] = False
                heappush(rooms, end_room)

            if len(ending) == n:
                end_time, end_room = heappop(ending)
                start, end = end_time, end_time + (end - start)
                using[end_room] = False
                heappush(rooms, end_room)
                while ending and ending[0][0] == end_time:
                    _, end_room = heappop(ending)
                    using[end_room] = False
                    heappush(rooms, end_room)
            while rooms and using[rooms[0]]:
                heappop(rooms)
            use_room = heappop(rooms)
            using[use_room] = True
            held[use_room] += 1
            heappush(ending, (end, use_room))

        return held.index(max(held))

# @l c code=end

