"""
Defining a function to calculate the list of non-prime numbers within the 
interval of arguments passed.
"""
def non_prime_list(x,y):
    # Declaring an empty list to store the list of non-prime numbers
    ans_list = []
    for i in range(x,y+1):
        # Avoiding the 1, because its not a prime number
        if i>=1:
            for j in range(2, i):
                # Checking if the number is non-prime i.e divisible by one of the values in the range
                if i%j == 0:
                    # If non-prime, appending it to our ans_list
                    ans_list.append(i)
                    # Using break to avoid repetition of same values in the ans_list
                    break
    return ans_list

"""
Defining a function to sort the given numbers and print the final ans_list 
in ascending order with just 10 elements per line
"""
def sortnprint(a,b):
    # Setting minimum and maximum value
    mini = min(a,b)
    maxi = max(a,b)
    final_list = non_prime_list(mini,maxi)
    for i in range(0, len(final_list), 10):
        print(final_list[i:i+10])

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Checking whether the input is numeric and declaring them as integer
if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    sortnprint(num1, num2)
else:
    print("The input value cannot be non-numeric or negative")
    

