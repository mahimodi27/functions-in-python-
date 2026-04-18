import math

def finding_factorials(numbers):
    result= map(math.factorial,numbers)
    return list(result)

user_input= input("enter non negative with space in between")

final_input=[int(x) for x in user_input.split()]

final_result= finding_factorials(final_input)

print("the final factorial list is:",final_result)
