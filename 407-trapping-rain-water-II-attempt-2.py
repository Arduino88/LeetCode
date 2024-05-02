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
        
    print(f'Matrix Columns: {len(row)}, Matrix Rows: {len(matrix)}')
    print(matrix[1][3])

def isValid(row, col, matrix, visited):
    if matrix[row][col] == 1:
        return False
    
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return None
    
    if visited[row][col]:
        return False
    
    return True

def DFS(row, column, matrix, visited, totalArea = 0):
    dRow = [0, 1, 0, -1]
    dCol = [-1, 0, 1, 0]
    
    st = []
    st.append([row, column])
    
    while len(st) > 0:
        print('totalArea:', totalArea)
        row, column = st.pop()
        
        
        print(f"ROW: {row}, COLUMN: {column}")
        valid = isValid(row, column, matrix, visited)
        print(f"is valid? {valid}")
        
        printMatrix(matrix)
        
        
        if valid is None:
            for row in range(len(matrix)):
                for column in range(len(matrix[0])):
                    if visited[row][column]:
                        matrix[row][column] = 1
            
            
            #return None, visited
        
        if not valid:
            continue
        
        
        visited[row][column] = True
        totalArea += 1
        print('TOTAL AREA INCREMENT TO:', totalArea)
        
        for i in range(4):
            
            newRow = dRow[i] + row
            newCol = dCol[i] + column
            st.append([newRow, newCol])
            
    print("Total Area:", totalArea)
    return totalArea, visited
            
            


def searchLayer(tensor, heightIndex) -> int:
    matrix = tensor[heightIndex]
    
    print('')
    printMatrix(matrix)
    
    total = 0
    visited = [[False] * len(matrix[0]) for i in range(len(matrix))]
    
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == 0:
                fill, visited = DFS(row - 1, column - 1, matrix, visited)
                print('FILL:', fill)
                if fill is None:
                    continue
                if fill is not None:
                    total += fill
                    
    
    return total
    

class Solution:

    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        
        yWidth = len(heightMap[0])
        xWidth = len(heightMap)
        
        
        
        maxHeight = 0
        for i in heightMap:
            maxHeight = max(max(list(map(lambda x : max(i), i))), maxHeight)
        
        tensor = [[[0 for _ in range(yWidth)] for _ in range(xWidth)] for _ in range(maxHeight)]
        print(f"maxHeight: {maxHeight}, yWidth: {yWidth}, xWidth: {xWidth}")
        
        
        for height in range(maxHeight):
            for x in range (xWidth):
                for y in range(yWidth):
                    
                    if heightMap[x][y] > height:
                    
                        print(height, x, y)
                        tensor[height][x][y] = 1
                        pass
        
        
        printTensor(tensor)
        return(searchLayer(tensor, 2))
    
    
    
    
        

        
sol1 = Solution()

visited = [[False] * 5 for i in range(5)]     
print(DFS(3, 3, [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]], visited))



print(sol1.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
#print(sol1.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]))