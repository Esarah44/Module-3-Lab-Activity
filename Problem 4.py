#Compute the area of a circle
#Created by Sara Hernandez
#October 16, 2022
#The purpose of this program is to greet the user using their name

#Below ask the user to enter the radius.
radius = input('Enter radius:')     # You can do it at once: radius = int(input("Enter a radius: "))

#Below will calculate the area of the circle.
circle_area = 3.1416*(int(radius)**2)

#Below will print the area of the circle.
print('The area of a circle with radius, ' + str(radius) + ', is ' + str(circle_area) + '.')
#using a format: print("The area of a circle with radius {} is {}.".format(radius, area))
