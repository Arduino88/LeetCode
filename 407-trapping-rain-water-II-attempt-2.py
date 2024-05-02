def printTensor(tensor):
    for i in range(len(tensor[0])):
        returnString = ''
        for height in range(len(tensor)):
            returnString += str(tensor[height][i])
            returnString += ' '
        print(returnString)

def printMatrix(matrix):
    for row in matrix:
        print(row)
        
    #print(f'Matrix Columns: {len(row)}, Matrix Rows: {len(matrix)}')

def inBounds(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return False
    return True
    

def isContained(initialRow, initialColumn, matrix, dfsVisual, visited):
    tempTally = 0
    dRow = [0, 1, 0, -1]
    dCol = [-1, 0, 1, 0]

    st = []
    st.append([initialRow, initialColumn])
    
    while len(st) > 0:
        #print('totalArea:', totalArea)
        row, column = st.pop()
        
        if dfsVisual[row][column] == True:
            continue
        
        dfsVisual[row][column] = True
        visited[row][column] = True
        tempTally += 1
        
        #printMatrix(dfsVisual)
        
        #print(f"ROW: {row}, COLUMN: {column}")
        
        
        
        for i in range(4):
            newRow = dRow[i] + row
            newCol = dCol[i] + column
            if inBounds(newRow, newCol, matrix):
                if matrix[newRow][newCol] == 0:
                    st.append([newRow, newCol])
            else:
                for i in range(len(dfsVisual)):
                    for j in range(len(dfsVisual[0])):
                        if dfsVisual[i][j] is True and visited[i][j] is True:
                            dfsVisual[i][j] = False
                #print('Searched Matrix:')
                #printMatrix(matrix)
                #print('')
                #print('Display Matrix:')
                #printMatrix(dfsVisual)
                #print(f'{initialRow}, {initialColumn} is not contained')
                tempTally = 0
                return False, tempTally, visited
        
        
        

        
    #print('')
    #printMatrix(dfsVisual)
    #print('')
    #print(f'{initialRow}, {initialColumn} is contained')
    return True, tempTally, visited

            
            


def searchLayer(tensor, heightIndex) -> int:
    matrix = tensor[heightIndex]
    dfsVisual = tensor[heightIndex]
    visited = [[False] * len(matrix[0]) for i in range(len(matrix))]
    #print('')
    #printMatrix(matrix)
    
    total = 0
    
    
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == 0 and visited[row][column] is False:
                #print(f"Starting DFS, layer: {heightIndex}, column: {column}, row {row}")
                
                is_contained, tally, visited = isContained(row, column, matrix, dfsVisual, visited)
                #print(visited)
                if is_contained:
                    total += tally
                    
    
    return total
    

class Solution:

    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        
        yWidth = len(heightMap[0])
        xWidth = len(heightMap)
        finalTally = 0
        
        
        maxHeight = 0
        for i in heightMap:
            maxHeight = max(max(list(map(lambda x : max(i), i))), maxHeight)
        
        tensor = [[[0 for _ in range(yWidth)] for _ in range(xWidth)] for _ in range(maxHeight)]
        #print(f"maxHeight: {maxHeight}, yWidth: {yWidth}, xWidth: {xWidth}")
        
        
        # encode tensor with data
        for height in range(maxHeight):
            for x in range (xWidth):
                for y in range(yWidth):
                    if heightMap[x][y] > height:
                        #print(height, x, y)
                        tensor[height][x][y] = 1
                        pass
        
        
        #printTensor(tensor)
        for layer in enumerate(tensor):
            print(layer[0])
            increase = searchLayer(tensor, layer[0])
            finalTally += increase
            #printMatrix(layer[1])
            #print(f'After searching layer {layer[0]}, finalTally increased by {increase} to {finalTally}')
            
    
        return finalTally
    
        

        
sol1 = Solution()

visited = [[False] * 5 for i in range(5)]     


print(sol1.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
print(sol1.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]))
print(sol1.trapRainWater([[14,17,18,16,14,16],[17,3,10,2,3,8],[11,10,4,7,1,7],[13,7,2,9,8,10],[13,1,3,4,8,6],[20,3,3,9,10,8]]))
print(sol1.trapRainWater([[19383,10886,12777,16915,17793,18335,15386,10492,16649,11421],[12362,27,8690,59,7763,3926,540,3426,9172,5736],[15211,5368,2567,6429,5782,1530,2862,5123,4067,3135],[13929,9802,4022,3058,3069,8167,1393,8456,5011,8042],[16229,7373,4421,4919,3784,8537,5198,4324,8315,4370],[16413,3526,6091,8980,9956,1873,6862,9170,6996,7281],[12305,925,7084,6327,336,6505,846,1729,1313,5857],[16124,3895,9582,545,8814,3367,5434,364,4043,3750],[11087,6808,7276,7178,5788,3584,5403,2651,2754,2399],[19932,5060,9676,3368,7739,12,6226,8586,8094,7539]]))