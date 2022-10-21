#Calculated the miles per gas for a car
#Created by Sara Hernandez
#October 16, 2022
#The purpose of this program is to greet the user using their name

#Below ask the user to enter the number of miles driven.
miles = input('Enter number of miles driven: ')  #miles = float(input("Miles drive: "))

#Below ask user to enter the number of gallons used.
gas = input('Enter number of gallons used: ')   #gas = float(input("Gas consumed :"))

#Belwo calculates the miles per gas.
mpg = int(miles)/int(gas)              

#Below prints the output of the miles per gas.
print('The MPG (Miles per Gas) is ' + str(mpg) + '.')
