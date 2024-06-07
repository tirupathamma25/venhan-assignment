def frequency_of_each_chr(sentence):
    sentence = sentence.replace(" ","")
    unique_letters = set(sentence)
    for i in sorted(unique_letters):
        count = sentence.count(i)
        print("{} : {}".format(i, count))
    
sentence = input()
frequency_of_each_chr(sentence)
