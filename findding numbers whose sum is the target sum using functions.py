def find_pairs_with_sum(numbers,target_sum):
    pairs=[]

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i]+ numbers[j]== target_sum:
                pairs.append((numbers[i],numbers[j]))

    return pairs


user_input=input("enter numbers with spaces in between")
final_list= [int(x) for x in user_input.split()]
targeted_sum= int(input("enter your target sum"))

result= find_pairs_with_sum(final_list,targeted_sum)

print(result)




