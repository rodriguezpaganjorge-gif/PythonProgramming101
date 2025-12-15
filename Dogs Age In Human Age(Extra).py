# Author: Jorge Rodriguez Pagan
# Dogs Age In Human Years (Calculator)

# How old is your dog in human years?
# Dog's Age in HUman Years: DogAge x 7.3

# 1. Input
sDogAge = input("What is your dogs Age?")
sDogAge2 = input("What is second your dogs Age?")


# 2. Convert Data
iDogAge = int(sDogAge)
iDogAge2 = int(sDogAge2)


# 3. Perform Calculation
iHumanAge= iDogAge * 7.3
iHumanAge2= iDogAge2 * 7.3

# 4. Output 
print("Your dog's age in human years is: " + str(iHumanAge))
print("Your dog's age in human years is: " + format(iHumanAge, '.2f'))

print("Your dog's age in human years is: " + str(iHumanAge2))
print("Your second dog's age in human years is: " + format(iHumanAge2, '.2f'))

# 1. Input
#iDogAge = int( input("What is your dog age?") )
#print("Your dog's age in human years is: " + format(iDogAge * 7.3, '.1f'))


# One liner dog age calc
#print ("Your dog's age in human years is: " + format(int(input("What is your dogs age?")) * 7.3, '.1f'))


# Formating
sDogName = input("What is your dog's name?")
sDogName2 = input("What is your second dog's name?")

print ("Your dog's name is: ", format(sDogName, "2") + format(iHumanAge, '1f'))
print ("Your dog's name is: ", format(sDogName2, "2") + format(iHumanAge2, '20f'))
