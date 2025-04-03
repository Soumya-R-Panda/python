from scipy.special import factorial
from decimal import Decimal

n=int(input("Enter a Number:- "))
print(f"Factorial of {n} is:- {Decimal(factorial(n))}")

