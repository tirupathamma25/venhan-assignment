def is_polindrome(word):
    reverse_string = ""
    for i in word:
        reverse_string = i + reverse_string
    if word == reverse_string:
        return"Polindrome"
        
    return "Not a Polindrome"

string = input()
print(is_polindrome(string))
