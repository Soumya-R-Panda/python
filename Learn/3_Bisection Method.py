import numpy as np

def f(x):
    return x**3 - 2*x + 2  

def bisection():
    a = float(input("Enter your lower guess:- "))
    b = float(input("Enter your upper guess:- "))
    tol = 10**-8
    if f(a) * f(b) >= 0:
        print("Try a different interval")
        return 0

    count = 0
    while (b - a) / 2 > tol:
        c = (a + b) / 2 
        if f(c) == 0:
            return c, count
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        count += 1

    return (a + b) / 2, count

root, count_num = bisection()
print("Root:- " , root)
print("Iterations:- " , count_num)
