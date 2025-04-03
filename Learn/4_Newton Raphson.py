import numpy as np

def f(x):
    return x**3 - 2*x + 2

def df(x):
    return 3*x**2 - 2

def newton_raphson():
    x = float(input("Enter your guess:- "))
    tol = 10**-8
    max_iter = 100
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            print("Choose a different starting point.")
            return None
        
        x_1 = x - (fx / dfx)
        
        if abs(x_1 - x) < tol:
            return x_1, i + 1
        x = x_1
    
    return x, max_iter


root, iteration_count = newton_raphson()
print("Final Root:- " , root )
print("Total Iterations:- " , iteration_count )
