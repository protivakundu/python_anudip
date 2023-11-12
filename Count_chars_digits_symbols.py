string="P@#yn26at^&i5ve"

#Takes all count variables
chars_count=0
digits_count=0
symbols_count=0

#For loop using
for i in string:
    if i.isalpha():
        chars_count=chars_count+1
    elif i.isdigit():
        digits_count=digits_count+1
    else:
        symbols_count=symbols_count+1

print("The number of characters is:",chars_count)
print("The number of digits is:",digits_count)
print("The number of symbols is:",symbols_count)