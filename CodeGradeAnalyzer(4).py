# Author: Jorge Rodriguez
# Class: Python Programming
# Purpose: Grade Analyzer

#ask for student name
s_name = input("Name of student that we are calculating the grades for: ")

#ask for test scores
itest1 = int(input("Test 1: "))
itest2 = int(input("Test 2: "))
itest3 = int(input("Test 3: "))
itest4 = int(input("Test 4: "))

#scores
tests = [itest1, itest2, itest3, itest4]

#grade droping lowest
g_drop = input("Do you wish to Drop the Lowest Grade Y or N? ")

if g_drop == "Y":
    lowest = min(tests)
    tests.remove(lowest)
    print("Dropping the lowest grade:", lowest)
    
#average
average = sum(tests) / len(tests)

#determine grade
if average >= 90:
    letter = "A"
elif average >= 80:
    letter = "B"
elif average >= 70:
    letter = "C"
elif average >= 60:
    letter = "D"
else:
    letter = "F"
    
#displaying the students results
    
print(s_name, "test average is:", average)
print("Letter Grade for the test is:", letter)
