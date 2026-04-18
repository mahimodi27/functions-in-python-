def common_numbers_twolists(list1,list2):
    setA= set(list1)
    setB= set(list2)

    common= setA & setB

    result= list(common)

    return result

input1=input("enter numbers with space in between")
listA= [int(x) for x in input1.split()]

input2 = input("enter numbers with space in between")
listB= [int(x) for x in input2.split()]

final_result= common_numbers_twolists(listA,listB)

print("common numbers are:",final_result)

    
