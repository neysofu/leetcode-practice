def intervalsOverlap(inter1, inter2):
    if inter1[0] > inter2[0]:
        inter1, inter2 = inter2, inter1
    return inter1[1] > inter2[0]

class Solution:
    def minMeetingRooms(self, intervals) -> int:
        numRooms = 0
        for interval in intervals:
            numConcurrentMeetings = 0
            for otherInterval in intervals:
                if intervalsOverlap(interval, otherInterval):
                    numConcurrentMeetings += 1
            numRooms = max(numConcurrentMeetings, numRooms)
        return numRooms