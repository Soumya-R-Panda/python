n = int(input("Enter a Number:- "))

def sqrt1(n):
    guess = n/2
    
    while True:
        if guess * guess - n == 0 :
            print(f"Square Root of {n} = {guess}")
            break
        else:
            guess = 0.5*(guess+(n/guess))
sqrt1(n)