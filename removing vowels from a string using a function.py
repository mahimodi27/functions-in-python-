def removing_vowels(input_string):
    vowels="aeiouAEIOU"
    result=" "

    for char in input_string:
        if char not in vowels:
            result+= char

    return result

user_input=input("enter a string")

final= removing_vowels(user_input)

print("the final string with removed vowels is:", final)

    
