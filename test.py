
M = [
[1, 2, 3], 
[4, 5, 6],
[7, 8, 9]
]

print(M[0][0]+M[1][1]+M[2][2])



def sum_of_diogonals(matrix):
    total=0
    for i in range(len(matrix)):
        total+=matrix[i][i]
        
    return total

print(sum_of_diogonals(M))