def is_prime(n):
    if n<2:
        return false
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return false
        return true

def remove_prime(numbers):
    result= list(filter(lambda x:not is_prime(x),numbers))
    return result

user_input= input("enter a list of numbers seperated by spaces")

try:
    num_list=[int[x] for x in user_input.split(x)]

    non_primes= remove_primes(num_list)

    print(f"original list: {num_list}")
    print(f"list with prime numbers removed: {non_primes}")

except valueerror:
    print("Invalid Input")
    
