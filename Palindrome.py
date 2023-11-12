##Input from user
string=str(input("Enter the string:"))

#Take an empty string
str1=""

#For loop using to find reverse
for i in string:
   str1=i+str1

#If statement for comapere strings
if string==str1:
    print("The string is Palindrome")
else:
    print("The string is not Palindrome")
