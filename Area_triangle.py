first_side=8
second_side=6
third_side=10
semi_perimeter=(first_side+second_side+third_side)/2
area=(semi_perimeter*(semi_perimeter-first_side)*(semi_perimeter-second_side)*(semi_perimeter-third_side))**0.5
print("The area of the trianle is:",area)