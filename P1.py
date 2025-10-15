#Area of the square wire
angle=60
radius=42

arc_length=(angle/360)*2*3.14*radius
side=arc_length/4 #as arc length=perimeter of square=4*side
area=side*side

print("length of wire:",arc_length)
print("area of square:",area)