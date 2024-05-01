class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        
        height = len(heightMap)
        width = len(heightMap[0])
        
        north = [[]]
        east = [[]]
        south = [[]]
        west = [[]]
        
        # populate north matrix

        
            
        
        

        # populate east matrix

        for y in range(height):
            for x in range(width):
                print('east:', x, y) 
                
                


        # populate south matrix



        # populate west matrix

        for y in reversed(range(height)):
            for x in reversed(range(width)):
                print('west:', x, y) 

        
    
    
    
    
sol1 = Solution()

print(sol1.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))