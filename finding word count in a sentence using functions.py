def count_word_frequency(sentence):
    words=sentence.split()

    frequency_dict={}

    for word in words:
        word=word.lower()
        
        if word in frequency_dict:
            frequency_dict[word]+=1

        else:
            frequency_dict[word]=1

    return frequency_dict

user_input=input("enter a sentence")

result= count_word_frequency(user_input)

print("word frequencies", result)
