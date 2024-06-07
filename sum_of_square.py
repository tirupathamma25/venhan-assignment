def sum_of_squares(lists):
    sum_of_squares = 0 
    for i in lists:
        sum_of_squares += i ** 2 
    return sum_of_squares    

numbers = [2, 3, 8, 5, 4]
print(sum_of_squares(numbers))