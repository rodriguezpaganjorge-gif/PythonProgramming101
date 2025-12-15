# Author: Jorge Rodriguez 
# Class: Python Programming - CIT-115-D02
# Purpose: calculate compund interest

fStarting_Salary= float(input("Enter your starting principal: "))
fAnnual_Interest_Rate= float(input("Enter the annual interest rate: "))
iInterest_Compound= int(input("How many times per year is the interest compounded?"))
iEarning_Interest= int(input("For how many years will the account earn interest? "))
rate = fAnnual_Interest_Rate / 100

# Compound Interest Formula:
# FV= PV * (1 + r/m)^(m*t)
fNew_Balance = fStarting_Salary * (1 + rate / iInterest_Compound)
(iInterest_Compound * iEarning_Interest)

print("At the End of the", iEarning_Interest, "years will be: $", round(fNew_Balance, 2))
