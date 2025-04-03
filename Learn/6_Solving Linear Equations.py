A = [[0.02, 0.01, 0, 0],[1, 2, 1, 0],[0, 1, 2, 1],[0, 0, 100, 200]]
B = [0.02, 1, 4, 800]

def solve(A, B):
    n = len(A)
    
    A_new = []
    for i in range(n):
        A_new.append(A[i] + [B[i]])
        # Augmented matrix bana liya, means A aur B ko jodna

    for i in range(n):
        diag = A_new[i][i]
        for j in range(i, n+1):
            A_new[i][j] = A_new[i][j] / diag
            # ye diagonal elements ko 1 karne ke liye

        for k in range(i+1, n):
            new = A_new[k][i]
            for j in range(i, n+1):
                A_new[k][j] = A_new[k][j] - new * A_new[i][j]
                # ye saare diagonal elements ke niche wala elements ko 0 kardega
                # So, ab hame ek upper triangular matrix milgaya

    x = [0] * n        # ye ek list banayega jiske andar n times zero bhardega
    for i in range(n-1, -1, -1):      # hum yahan range n-1 se 0 tak jaa rahe hai, kyunki last row se back substitution karke solve karna hota hai (as in last row, there will be only 1 element)
        x[i] = A_new[i][n]
        for j in range(i+1, n):
            x[i] = x[i] - ( A_new[i][j] * x[j] )

    return x

solution = solve(A, B)
print("Solution:", solution)
