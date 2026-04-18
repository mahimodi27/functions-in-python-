def find_palindrome(numbers):
    palindrome_lst=[]

    for num in numbers:
        lst= str(num)
        if lst==lst[::-1]:
            palindrome_lst.append(num)

    return palindrome_lst

user_input=input("enter numbers in the list")

num_list= [int(x) for x in user_input.split()]

palindromes= find_palindrome(num_list)

print("the palindromes are:",palindromes)

    
