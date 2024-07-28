class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        #print(intervals)
        returnList = []

        while intervals:
            #print(f'starting loop, intervals: {intervals}')
            temp = [intervals.pop(0)]
            maximum = temp[0][1]
            while intervals and maximum >= intervals[0][0]:
                temp.append(intervals.pop(0))
                maximum = max(maximum, temp[-1][1])
                #print(f'popping... temp: {temp}')

            returnList.append([temp[0][0], maximum])
            temp.clear()

        return returnList