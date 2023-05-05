"""
Defining a function for checking whether the given string is palindrome or not
by reversing the given string and comparing it with the original string
"""
def palindrome(str1):
    strrev = str1[::-1]
    if(str1 == strrev):
        # If yes, returning true
        return True
    else:
        # Otherwise, returning false
        return False

"""
Defining a function to convert the given string to uppercase and to get 
the highest occurring letter/digit from the given string
"""
def freq_chars(str2):
    str2 = str2.upper()
    print("The given string converted to uppercase: ",str2)
    # Declaring an empty dictionary to store the occurrence of the letters and digits in a string
    freq = {}
    for i in str2:
        # If the letter/digit is already a key in the dictionary, incrementing its value by 1
        if i in freq:
            freq[i] += 1
        # If the letter/digit is absent in the dictionary, adding it as a key
        elif(i.isalnum()):
            freq[i] = 1
        # If its not a letter/digit, ignoring it and proceeding the iteration
        else:
            continue
    # Calculating the highest occurring key by taking the maximum of their values
    highestkey = max(freq, key=freq.get)
    return highestkey

""" 
Defining a function to count the occurence of letters, digits and spaces in the
given string
"""
def dictcounts(str3):
    counts_dict = {'letters' : 0, 'spaces' : 0, 'digits' : 0}
    for i in str3:
        # If the character is a digit, incrementing its value by 1
        if i.isdigit():
            counts_dict['digits'] += 1
        # If the character is a letter, incrementing its value by 1
        elif i.isalpha():
            counts_dict['letters'] += 1
        # If the character is a space, incrementing its value by 1
        elif i.isspace():
            counts_dict['spaces'] += 1
        # Ignoring if the character is not digit/letter/space
        else:
            continue
    return counts_dict