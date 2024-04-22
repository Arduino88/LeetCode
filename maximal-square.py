from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

#Maximal Square in a matrix algorithm

class Matrix:
    def __init__(self, width):  # added height parameter
        self.width = width  # default to square matrix
        self.matrix = [[1 for _ in range(width)] for _ in range(width)]
    
    def debugPrint(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])
            
def biggest_square_at(yard: Matrix, row: int, column: int, output: Matrix):
    if yard.matrix[row][column] == 0:
        return 0
    elif row == 0 or column == 0:
        return yard.matrix[row][column]
    
    else:
        return min(output.matrix[row][column-1], output.matrix[row-1][column-1], output.matrix[row-1][column]) + 1
        

#INPUT
#------------------------------------------------------------------------

width = int(input())
tree_count = int(input())
yard = Matrix(width)
dp = Matrix(width)


for i in range(tree_count):
    tree = input().split()
    tree[0], tree[1] = int(tree[0]) - 1, int(tree[1]) - 1
    yard.matrix[tree[0]][tree[1]] = 0

#CALCULATION
#-----------------------------------------------------------------------

for row in range(width):
    for column in range(width):
        dp.matrix[row][column] = biggest_square_at(yard, row, column, dp)
        
#OUTPUT
#------------------------------------------------------------------------

print('Yard:')
yard.debugPrint()
print('DP:')
dp.debugPrint()

df = pd.DataFrame(dp.matrix)
# create matplotlib color chart

print(df)


# Plot the DataFrame as a heatmap
plt.figure(figsize=(10, 6))
plt.pcolor(df, cmap='Blues', edgecolors='white')
plt.title("Heatmap of DataFrame")
plt.show()