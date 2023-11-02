distance=int(input("Enter the distance:"))
if distance<=50:
    print("The charges are:",distance*8)
elif distance>=51 and distance<=100:
    print("The charges are:",distance*10)
else:
    print("The charges are:",distance*12)