#Author: Jorge Rodriguez :)
#Class: Python Programming
#Purpose: Compound Interest With Loops

# Collecting Data

iOD=int(input("What is the Original Deposit (postive value):"))
fInterest=float(input("What is the Interest Rate(postive value):"))
iNOM=int(input("What is the Number of Months?(postive value):")) #NOM= Number of Months
fGoalAmount=float(input("What is the Goal Amount?(can enter 0 but not negative):"))

if fGoalAmount <=0:
    print("Input must be 0 or greater")
    fGoalAmount=float(input("What is the Goal Amount?(can enter 0 but not negative):"))
    
#Formula Format
balance = float(iOD)
monthlyRate = (fInterest / 100) / 12

# Monthly Loop based on Goal Amount

for month in range(1, iNOM + 1):
    balance = balance * (1 + monthlyRate)
    print("Month:", month, "Account Balance is: $", format(balance, ".2f"))
    
if fGoalAmount > 0:
    balance2 = float(iOD)
    count = 0 # count for goal amount months
    
    while balance2 < fGoalAmount:
        balance2 = balance2 * (1 + monthlyRate)
        count += 1

    print("\nIt will take:", count, "months to reach the goal of: $", format(fGoalAmount, ".2f"))
