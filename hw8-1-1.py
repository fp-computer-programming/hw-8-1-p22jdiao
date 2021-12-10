# Author: JD 12/09/2021

"""
Write a Python program that will prompt the user to enter the radius and height of a cylinder, 
calculate the surface area and volume of the cylinder, and then display the results. 
Hint: Volume of a cylinder = π r 2 h and Surface Area of a cylinder = 2 π r (h + r)
"""
import math as m

def cylinder_calculator(radius, height):
    volume = int(m.pi * radius * height)
    surface = int(2 * m.pi * radius * (height + radius))
    
    result = [volume, surface]
    return result
    
r = input("Enter the radius: ")
r = int(r)

h = input("Enter the height: ")
h = int(h)
    
v = cylinder_calculator(r, h)[0]

s = cylinder_calculator(r, h)[1]

print("The volume is {0} and the surface is {1}".format(v,s))

#test

print(cylinder_calculator(0,0) == [0, 0])
print(cylinder_calculator(3,0) == [0, 56])
print(cylinder_calculator(5,5) == [78, 314])