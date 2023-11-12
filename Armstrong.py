#Input from user
num=int(input("Enter the number:"))

#Convert the number into string
str_num=str(num)
count=len(str(num))

total=0

#For loop using 
for i in str_num:
   total=total+pow(int(i),count)

#If statement using for comparing
if num==total:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")