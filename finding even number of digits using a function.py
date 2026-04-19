def length_even(input_str):
    result=[]

    for num in input_str:
        if len(str(num))%2==0:
            result.append(num)
    return result

user_input=input("enter numbers with spaces in between")
num_list= [int(x) for x in user_input.split()]

final= length_even(num_list)

print("the list with even digits of number is", final)
