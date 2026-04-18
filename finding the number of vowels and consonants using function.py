def count_vowels_consonants(text):
    vowels= "aeiouAEIOU"
    vowel_count= 0
    consonant_count=0

    for char in text:
        if char.isalpha:
            if char in vowels:
                vowel_count= vowel_count+1
            else:
                consonant_count= consonant_count+1

    return vowel_count, consonant_count


user_input= input("Enter a string")

v_total,c_total= count_vowels_consonants(user_input)

print("the number of vowels are", v_total)

print("the number of consonants are", c_total)

