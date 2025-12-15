#Class: Python Programming
#Purpose: Code Lists Real Estate Analyzer
#Author: Jorge Rodriguez Pagan



#getFloat Input :)

def getFloatInput(prompt):
    while True:
        value= input(prompt)
        try:
            number= float(value)
            if number <= 0:
                print("Error: Enter a number higher than 0.")
            else:
                return number
        except ValueError:
                print("Error: numbers only. Please try again.")

#defining Median Input :3 
                
def Median(values):  
    n= len(values)
    if n%2 == 1: #odd
        return values [n//2-1]
    else: #even
        mid1= values[n//2-1]
        mid2=values[n//2]
        return (mid1 + mid2) / 2

#defining the main hub >.<
    
def main():
    sales= []
    again= "Y"

    while again.upper () == "Y":
        price= getFloatInput ("Enter propety sales value:")
        sales.append(price)

        again = input("Enter another value Y or N: ")
        while again.upper() not in ("Y", "N"):
            again = input ("Enter another value Y or N:")

    print() 

    sales.sort()

    for i in range(len(sales)):
           print("Property", i + 1, "$", format(sales[i], ",.2f"))

    print()

    minimum = min(sales)
    maximum = max(sales)
    total = sum(sales)
    average = total/len(sales)
    median = Median(sales)
    commission= total * 0.003

    print ("Minimum:  $", format(minimum, ",.2f"))
    print ("Maximum:  $", format(maximum, ",.2f"))
    print ("Total:  $", format(total, ",.2f"))
    print ("Average:  $", format(average, ",.2f"))
    print ("Median:  $", format(median, ",.2f"))
    print ("Commission:  $", format(commission, ",.2f"))
main()
