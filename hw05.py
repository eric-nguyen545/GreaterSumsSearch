def greater_by_one_for(a_string):
    '''
    Purpose:
        Increase the digits in the string by one, and if it is a 9 back to zero
    Parameters:
        a_string: a string that the user inputs that contains only numbers
    Return Value:
        A string with each digit increased by one from the original, and if it is a 9 it is zero
    '''
    new_string = ''
    for char in a_string:
        if char == '9':
            new_string += '0'
        else:
            new_string += str(int(char) + 1)
    return new_string

def greater_by_one_while(a_string):
    '''
    Purpose:
        Increase the digits in the string by one, and if it is a 9 back to zero
    Parameters:
        a_string: a string that the user inputs that contains only numbers
    Return Value:
        A string with each digit increased by one from the original, and if it is a 9 it is zero
    '''
    new_string = ''
    i = 0
    while i < len(a_string):
        if a_string[i] == '9':
            new_string += '0'
        else:
            new_string += str(int(a_string[i]) + 1)
        i += 1
    return new_string

def count_of_sums(lower, upper, sum_val):
    '''
    Purpose:
        Find the total amount of ways to sum two integers
    Parameters:
        lower: an integer representing the bottom end of the searchable range
        upper: an integer representing the top end of the searchable range
        sum_val: the integer sum
    Return Value:
        The number of different ways two integers can be added up between the upper and lower bound to equal the sum value
    '''
    count = 0
    for i in range(lower, upper+1):
        for j in range(lower, upper+1):
            if i + j == sum_val:
                count += 1
    return count

def character_search(string_a, string_b, string_c):
    '''
    Purpose:
        Build a string containg all of the characters in string_a, and string_b but not in string_c
    Parameters:
        string_a: a string that specifes order of the return value
        string_b: a string that will be checked with string_a if any characters are the same
        string_c: a string that will exclude any characters found in string_a and string_b; also not included in the return value
    Return Value:
        The characters in string_a and string_b but not string_c in the order of string_a
    '''
    result = ''
    for i in range(len(string_a)):
        char = string_a[i]
        j = 0
        in_b = False
        k = 0
        in_c = False
        while not in_b and j < len(string_b):
            if char == string_b[j]:
                in_b = True
            j += 1
        while not in_c and k < len(string_c):
            if char == string_c[k]:
                in_c = True
            k += 1
        if in_b and not in_c:
            result += char
    return result
