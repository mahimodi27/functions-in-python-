def calculate_even_sum(numbers):
    total=0

    for num in numbers:
        if num%2==0:
            total+=num

    return total

user_input=input("Enter a list of integers sepearted by spaces")
final_list= [int(x) for x in user_input.split()]

result= calculate_even_sum(final_list)
print("the sum of even numbers is", result)

