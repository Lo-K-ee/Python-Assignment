# Importing the package for tabulating the list of tuples
from tabulate import tabulate

"""
Defining a function with three parameters - tuple with the employee details and 
salary ranges from minimum to maximum. 
Checking the given condition and appending the employees accordingly to their salaries.
"""
def emp_deats(tup1, minsal, maxsal):
    empl_table = []
    for row in tup1:
        if(int(row[2]) >= minsal and int(row[2]) <= maxsal):
            empl_table.append(row)
    # Checking if the list is empty after the iteration
    if(len(empl_table) == 0):
        print("There are no employee matching with the given salary intervals")
    # If the list is not empty then printing the tuples in table format
    else:
        return(tabulate(empl_table, headers=["Name", "Job title", "Salary"]))
        
"""
Defining a function to convert the contents of the file with employee details and
storing them as a tuple
"""
def filetotup():
    list_of_tuples = []
    while(True):
        file1 = input("Enter a file name which you would like to open: ")
        try:
            input_file = open(file1, "r")
            for line in input_file:
                # Stripping and splitting the values to store it in appropriate variables
                name, job_title, salary = line.strip().split(',')
                # Storing the values in the tuple
                tup_line = (name,job_title,salary)
                list_of_tuples.append(tup_line)
            input_file.close()
            break
        # If the entered file is not found, asking the user for a valid file
        except IOError:
            print(f"Can't find the file '{file1}', Try again")
    # Sorting the tuple based on the employee's salary in descending order
    sorted_tuple = sorted(list_of_tuples, key=lambda x: int(x[2]), reverse=True)
    return sorted_tuple

"""
A function to ask the user for salary range and
iterating with employee's decision - quit/continue.
"""
def begin(final_tuple):
    while True:
        print(final_tuple)
        mini_sal = int(input("Enter the minimum salary:"))
        maxi_sal = int(input("Enter the maximum salary:"))
        # Storing the tuple which lies between the salary range
        salary_table = emp_deats(final_tuple, mini_sal, maxi_sal)
        print(salary_table)
        # Prompting the user if he/she wants to quit the company or continue?
        decision = int(input("Do you wish to quit(1) or supply another salary range(2): "))
        # If he/she decides to quit(1) the program ends
        if(decision == 1):
            break
        # If he/she decides to continue(2), the program starts over with a different salary range
        elif(decision == 2):
            continue

# Getting the finalized tuple in descending order, storing it in desctuple
desctuple = filetotup()
begin(desctuple)
