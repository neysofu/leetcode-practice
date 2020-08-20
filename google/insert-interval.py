def intervalsAreDisjoint(inter1, inter2):
    return inter1[1] < inter2[0] or inter2[1] < inter1[0]

def mergeIntervals(inter1, inter2):
    return [min(inter1[0], inter2[0]), max(inter1[1], inter2[1])]

# [[1,3],[6,9]], newInterval = [2,5]
class Solution:
    def insert(self, intervals, newInterval):
        resultIntervals = []
        newIntervalWasInserted = False
        for interval in intervals:
            if newInterval[1] < interval[0] and not newIntervalWasInserted:
                resultIntervals.append(newInterval)
                newIntervalWasInserted = True
            if intervalsAreDisjoint(interval, newInterval):
                resultIntervals.append(interval)
            else:
                newInterval = mergeIntervals(interval, newInterval)
        if not newIntervalWasInserted:
            resultIntervals.append(newInterval)
        return resultIntervals