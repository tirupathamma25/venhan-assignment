def reverse_string(string):
    reverse_string = ""
    for i in string:
        reverse_string = i + reverse_string
    return reverse_string    

word = input()
result = reverse_string(word)
print(result)