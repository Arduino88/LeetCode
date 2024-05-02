def isValid(row, col, ROW, COL, vis, grid):
     
    # If cell is out of bounds
    if (row < 0 or col < 0 or row >= ROW or col >= COL):
        return None
 
    # If the cell is already visited
    #print(vis, row, col)
    if (vis[row][col]):
        return False
 
    # If the cell is marked 2
    if grid[row][col] == 2:
        return False
    
    # Otherwise, it can be visited
    return True


def DFS(row, col, grid, ROW, COL, vis):
    dRow = [0, 1, 0, -1]
    dCol = [-1, 0, 1, 0]
    # Initialize a stack of pairs and
    # push the starting cell into it
    st = []
    st.append([row, col])
 
    # Iterate until the
    # stack is not empty
    while (len(st) > 0):
        # Pop the top pair
        curr = st[len(st) - 1]
        st.remove(st[len(st) - 1])
        row = curr[0]
        col = curr[1]
 
        # Check if the current popped
        # cell is a valid cell or not
        valid = isValid(row, col, ROW, COL, vis, grid)
        
        if valid is None:
            return True, vis
        
        if not valid:
            continue
 
        # Mark the current
        # cell as visited
        vis[row][col] = True
 
        # Print the element at
        # the current top cell
        #print(grid[row][col], end = " ")
 
        # Push all the adjacent cells
        for i in range(4):
            adjx = row + dRow[i]
            adjy = col + dCol[i]
            st.append([adjx, adjy])
            
    return False, vis

class Solution:

    

    
    
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        
        
        
        height = len(heightMap)
        width = len(heightMap[0])
        
        
        vis = [[False for _ in range(width)] for _ in range(height)]
        
        
        north = [[0 for _ in range(width)] for _ in range(height)]
        east = [[0 for _ in range(width)] for _ in range(height)]
        south = [[0 for _ in range(width)] for _ in range(height)]
        west = [[0 for _ in range(width)] for _ in range(height)]
        resultMatrix = [[0 for _ in range(width)] for _ in range(height)]
        crossSection = [[0 for _ in range(width)] for _ in range(height)]
        
        # populate north matrix

        for y in range(width):
            for x in range(height):
                
                if x == 0:
                    north[x][y] = heightMap[x][y]
                    continue
                
                if north[x - 1][y] < heightMap[x][y]:
                    north[x][y] = heightMap[x][y]
                else:
                    north[x][y] = north[x - 1][y]
            
        
        for i in north: print('north:', i)
        print('')
        
        

        # populate east matrix

        for x in range(height):
            for y in range(width):
                
                if y == 0:
                    east[x][y] = heightMap[x][y]
                    continue
                
                if east[x][y - 1] < heightMap[x][y]:
                    east[x][y] = heightMap[x][y]
                else:
                    east[x][y] = east[x][y - 1]
                    
                
                    
        for i in east: print('east:', i)
        print('')

        # populate south matrix
        
        
        for y in range(width):
            for x in reversed(range(height)):
                
                if x == height - 1:
                    south[x][y] = heightMap[-1][y]
                    continue
                
                if south[x + 1][y] < heightMap[x][y]:
                    south[x][y] = heightMap[x][y]
                else:
                    south[x][y] = south[x + 1][y]
            
        
        for i in south: print('south:', i)
        print('')
        
        # populate west matrix

        for x in range(height):
            for y in reversed(range(width)):
                
                if y == width - 1:
                    west[x][y] = heightMap[x][-1]
                    continue
                
                if west[x][y + 1] < heightMap[x][y]:
                    west[x][y] = heightMap[x][y]
                else:
                    west[x][y] = west[x][y + 1]
        
        for i in west: print('west:', i)
        print('')
    
        combinedMatrix = [[0 for _ in range(width)] for _ in range(height)]
        
        for i in range(height):
            for j in range (width):
                combinedMatrix[i][j] = min(north[i][j], east[i][j], south[i][j], west[i][j])
                
                
        for i in combinedMatrix: print('combined:', i)        
        print('')
                
                
        # combine matrices        
                
        for i in range(height):
            for j in range (width):
                resultMatrix[i][j] = combinedMatrix[i][j] - heightMap[i][j]
    
        
    
        
        for i in heightMap: print('height map:', i)    
        
        print('total area:', sum([sum(i) for i in combinedMatrix]))
        
        for searchHeight in reversed(range(max([max(i) for i in heightMap]) )):
            for i in range(height):
                for j in range (width):
                    if heightMap[i][j] >= searchHeight:
                        crossSection[i][j] += 1
                        
                    if combinedMatrix[i][j] >= searchHeight:
                        crossSection[i][j] += 1
                    
            for i in crossSection: print('HEIGHT:', searchHeight, 'cross section:', i)     
            print('')
            
            for i in resultMatrix: print('result:', i)    
            print('')
            
            try:
                for i in range(height):
                    for j in range (width):
                        if crossSection[i][j] == 1:
                            print('DFS RUNNING')
                            leaky, visMatrix = DFS(i, j, crossSection, height, width, vis)
                            print(f"leaky: {leaky}")
                            for row in visMatrix: print(row)
                            if leaky:
                                raise StopIteration
        
            except StopIteration:
                for i in range(height):
                    for j in range(width):
                        print(f"visMatrix[i][j]: {visMatrix[i][j]}, resultMatrix[i][j]: {resultMatrix[i][j]}, heightMap[i][j]: {heightMap[i][j]}, searchHeight: {searchHeight}")
                        if visMatrix[i][j] == True and resultMatrix[i][j] + heightMap[i][j] >= searchHeight:
                            resultMatrix[i][j] -= 1
                    
            
            for i in resultMatrix: print('result after:', i)    
            print('')
        
        
        
        return(sum([sum(i) for i in resultMatrix]))
        
    
    
sol1 = Solution()

print(sol1.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]))