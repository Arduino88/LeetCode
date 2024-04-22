#Maximal Square in a matrix algorithm

class matrix:
    def __init__(self, width: int):
        self.height = width
        self.width = width
        self.matrix = {}
        for i in range(width):
            self.matrix[i] = {}
            for j in range(width):
                self.matrix[i][j] = 0
    
    def debugPrint(self):
        for i in self.matrix:
            print(self.matrix[i])

#INPUT
#------------------------------------------------------------------------

width = int(input())
tree_count = int(input())
yard = matrix(width)
dp = matrix(width)


for i in range(tree_count):
    tree = input().split()
    tree[0], tree[1] = int(tree[0]) - 1, int(tree[1]) - 1
    yard.matrix[tree[0]][tree[1]] = 1

#CALCULATION
#-----------------------------------------------------------------------

dp.matrix[0] = yard.matrix[0]

for i in range(yard.height):
    yard.matrix