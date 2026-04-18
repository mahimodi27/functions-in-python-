def reverse_words(sentence):
    words=sentence.split()
    #sentence.split() seperates different words into list of strings so they are easier to work with

    reversed_list=[word[::-1] for word in words]

    result= " ".join(reversed_list)

    return result

user_input=input("enter a sentence")

reversed_sentence= reverse_words(user_input)

print("the modified sentence is:",reversed_sentence)
