def number_divisible(num_list,k):
    divisible_list=[]

    for num in num_list:
        if num%k==0:
            divisible_list.append(num)
    return divisible_list

user_input= input("enter different numbers with space in between")

list_numbers= [int(x) for x in user_input.split()]

k_value= int(input("enter a value of k "))

result= number_divisible(list_numbers,k_value)

print("the list of numbers divisible by k are", result)
