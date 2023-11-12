string="Welcome to python Training"

#Take an empty list
vowels=[]
count=0

#For loop using for find vowels
for i in string:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        vowels.append(i)
        count=count+1

#Print all the requirements        
print("The vowels are:",vowels)
print("The number of vowels are:",count)