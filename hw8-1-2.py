# Author: JD 12/09/2021

def point_counter(three_points, two_points, free_throw):
    total = three_points * 3 + two_points * 2 + free_throw
    return total

thrp = int(input("Enter the number of three points: "))

twp = int(input("Enter the number of tow points: "))

ft = int(input("Enther the number of free throws: "))

result = point_counter(thrp, twp, ft)

print("The score is", result)

#test
print(point_counter(0, 0, 0) == 0)
print(point_counter(10, 10, 10) == 60)
print(point_counter(20, 20, 20) == 120)