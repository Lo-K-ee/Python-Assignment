# Importing datetime package to work with dates
import datetime
from datetime import date
from pickle import TRUE

# Defining the date formats in variables
American_d_format = '%m/%d/%Y'
European_d_format = '%d/%m/%Y'

dob = input("Enter your date of birth (in mm/dd/yyyy): ")

"""
Defining a function for validating the date fetched from the user, 
whether if its in American format or not, 
if its valid proceeding further to the function.
"""
def dob_validation(dob_input):
   try:
      validation = datetime.datetime.strptime(dob, American_d_format)

   except ValueError:
      print("Incorrect data format, should be mm/dd/yyyy")
   
   else:
      age_calc(dob_input)

# Defining a function to calculate the age of the person

def age_calc(validated_input):
      
      # Converting the given date into American format
      dobstrp = datetime.datetime.strptime(validated_input, American_d_format).date()\
      # Fetching today's date
      today = date.today()
      # Checking whether the input date is on the future, and printing error message accordingly
      if dobstrp > today:
         print("The DOB cannot be in the future")
      else:
         age = today.year - dobstrp.year
         # Checking whether the month & date are ahead in the future to deduct it from the age
         if(today.month, today.day) < (dobstrp.month, dobstrp.day):
            age -= 1
         # American date format
         print("The age of the person is ",age)
         # European date format
         euro_d = datetime.datetime.strptime(validated_input, American_d_format).strftime(European_d_format)
         print("The european format of the DOB is ", euro_d)

dob_validation(dob)

