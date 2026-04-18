def get_prime_factors(n):
    factors=[]
    #step 1: to remove all the 2's
    while n%2==0:
        factors.append(2)
        n=n//2

    #n must be odd at this point
    #start checking from 3

    divisor=3
    while divisor*divisor<=n:
        while n%divisor==0:
            factors.append(divisor)
            n=n//divisor
        divisor+=2


    #step 3: if the n is still not divided then it ia a prime number
    if n>2:
        factors.append(n)

    return factors

user_input=int(input("enter an integer that you wanna find prime factors of"))

result= get_prime_factors(user_input)

print("the prime factors are", result)

            
    
    
