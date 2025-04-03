pos_int = int(input("Enter A Number (greater than 6): "))
nums = []
n = 6
while ( n <= pos_int ):
    temp = []
    for i in range(1,n):
        if ( n % i == 0 ) :
            temp.append(i)
    sum = 0
    for k in temp:
        sum = sum + k
    if ( sum == n ) :
        nums.append(n)
    n += 1

print(nums)
