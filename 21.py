n = int(input())

if n == 0:
    print("Valid")
else:
    n = abs(n)
    valid = True
    
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            valid = False
            break
        n //= 10
    
    if valid:
        print("Valid")
    else:
        print("Not valid")
