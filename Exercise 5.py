import numpy as np

# Asking the user for a file name and verifying its presence
file_name = input("Enter the file name: ")
try:
    stu_file = open(file_name, "r")
except FileNotFoundError:
    raise FileNotFoundError("Error : Unable to find the file")
else:
    # Reading the line1 to get the no.of.students and coursework weightage 
    line1 = stu_file.readline().strip().split(" ")
    # Storing the number of students in num_of_stu variable
    num_of_stu = int(line1[0])
    stu_array = np.array([[0, 0.0, 0.0, 0.0]]*num_of_stu)
    # Storing the coursemark and calculating the exam marks
    cworkmarks = int(line1[1])
    exammarks = 100 - cworkmarks

# Declaring a stu_no variable to use it as index
stu_no = 0
for line in stu_file:
    # Splitting line by spaces and storing the each values
    values = line.split(" ")
    # Skipping the first line
    if line == 0:
        continue
    else:
        # Storing the values from the file to the array
        stu_array[stu_no][0] = int(values[0])
        stu_array[stu_no][1] = float(values[1])
        stu_array[stu_no][2] = float(values[2])
        stu_array[stu_no][3] = float(stu_array[stu_no][1] * (exammarks/100) + stu_array[stu_no][2] * (cworkmarks/100))
        stu_no += 1
print(stu_array)

"""
Defining a function to calculate the grade with three parameters - exam marks,
coursework marks and the overall marks
"""
def calc_grade(emark, cmark, total):
    grade = ''
    # If the exammark/coursemark is less than 30 - Fail
    if round(emark) < 30 or round(cmark) < 30:
        grade = 'Fail'
    # If the overall marks is above 70 - First class
    elif round(total) >= 70:
        grade = 'First-class'
    # If the overall marks is between 50 to 69 - Second class
    elif 50 <= round(total) <= 69:
        grade = 'Second-class'
    # If the overall marks is between 40 to 49 - Third class
    elif 40 <= round(total) <= 49:
        grade = 'Third-class'
    # If the overall marks is below 40 - Fail
    elif round(total) < 40:
        grade = 'Fail'
    return grade

# Defining a structured datatype 'stutype'
stutype = [('regnum', int), ('exammark', int), ('cworkmark', int), ('overall', int), ('grade', 'S15')]
s_details = np.array([], dtype=stutype)
# Creating a dictionary to print the occurrences of student grades
grade_dict = {'First-class' : 0, 'Second-class' : 0, 'Third-class' : 0, 'Fail' : 0, 'StuFailed' : [] }

# Iterating through the stu_array created from the values of the file
for i in stu_array:
    # Storing the values in appropriate variables
    regnum, exammark, cworkmark, overall = i
    stu_grade = calc_grade(exammark, cworkmark, overall)
    # Creating a tuple with the above variables
    stutuple = (regnum, exammark, cworkmark, overall, stu_grade)

    # Counting the grade of the students and storing the register number of failed students
    grade_dict[stu_grade] += 1
    if stu_grade == 'Fail':
        grade_dict['StuFailed'].append(int(regnum))
    
    # Generating the numpy array from the elements of tuple and appending the values
    tup_to_arr = np.array([stutuple], dtype=stutype)
    s_details = np.append(s_details, tup_to_arr, axis=0)

# Sorting the array with overall marks
sorted_list = np.sort(s_details, order='overall')[::-1]
print(sorted_list)

# Storing the array in the file
f = open('output_file_ex5.txt', 'w+')
print(sorted_list, file = f)
stu_file.close()
f.close()

# Printing to console
print(grade_dict)
