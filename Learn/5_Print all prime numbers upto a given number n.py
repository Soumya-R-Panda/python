n = int(input("Enter A Number:- "))

def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for j in range(2,n+1):
    if prime(j):
        print(j)
