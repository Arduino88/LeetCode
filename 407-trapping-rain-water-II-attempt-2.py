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
    

def isContained(initialRow, initialColumn, matrix, totalArea = 0):
    tempTally = 0
    dfsVisual = matrix.copy()
    visited = [[False] * len(matrix[0]) for i in range(len(matrix))]
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
                visited = [[False] * len(matrix[0]) for i in range(len(matrix))]
                #print('Searched Matrix:')
                #printMatrix(matrix)
                #print('')
                #print('Display Matrix:')
                #printMatrix(dfsVisual)
                #print(f'{initialRow}, {initialColumn} is not contained')
                tempTally = 0
                return False, tempTally
        
        
        

        
    #print('')
    #printMatrix(dfsVisual)
    #print('')
    print(f'{initialRow}, {initialColumn} is contained')
    return True, tempTally

            
            


def searchLayer(tensor, heightIndex) -> int:
    matrix = tensor[heightIndex]
    
    #print('')
    #printMatrix(matrix)
    
    total = 0
    
    
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == 0:
                #print(f"Starting DFS, layer: {heightIndex}, column: {column}, row {row}")
                
                is_contained, tally = isContained(row, column, matrix)
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
        
        
        printTensor(tensor)
        for layer in enumerate(tensor):
            print(f'In layer {layer[0]}:')
            increase = searchLayer(tensor, layer[0])
            finalTally += increase
            printMatrix(layer[1])
            print(f'After searching layer {layer[0]}, finalTally increased by {increase} to {finalTally}')
            
    
        return finalTally
    
        

        
sol1 = Solution()

visited = [[False] * 5 for i in range(5)]     


#print(sol1.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
#print(sol1.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]))
print(sol1.trapRainWater([[14,17,18,16,14,16],[17,3,10,2,3,8],[11,10,4,7,1,7],[13,7,2,9,8,10],[13,1,3,4,8,6],[20,3,3,9,10,8]]))