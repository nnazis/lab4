import math
num = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
area = int((num * length**2) / (4 * math.tan(math.pi / num)))
print(f"The area of the polygon: {area}")