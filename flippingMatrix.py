# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
matrix = [
    [9,1,2,2],
    [1,2,3,2],
    [3,3,4,4],
    [3,3,4,4]
]

def getQuads(matrix): 
    n = len(matrix)//2
    max_sum = 0
    for i in range(n): 
        for j in range(n): 
            print(i, j)
            max_sum += max( 
                    matrix[i][j], # top left
                    matrix[2*n - i - 1][j], # bottom left
                    matrix[i][2*n -j - 1],  # top right
                    matrix[2*n -i - 1][2*n -j - 1] # bottom right
            )
            
    print(f"\n {max_sum}")
       
    
getQuads(matrix)
    
    
