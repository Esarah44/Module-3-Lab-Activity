#This will tell you when you wil return from vacation
#Created by Sara Hernandez
#October 16, 2022
#The purpose of this program is to greet the user using their name

#Below will ask user to enter the starting day number of when the will begin their vacation.
start = input('Enter starting day number: ')

#Below will ask user to enter the length of their stay.
length = input('Enter length of your stay: ')

#Below will calculate the start and lengh of the vacation.
finish = int(start) + int(length)

#Below will calculate the remainder of Finish after dividing by 7 
return_day = finish % 7

#Below will print the return day.
print(return_day)   #print("Your returning date number is {}.".format(return_day))
