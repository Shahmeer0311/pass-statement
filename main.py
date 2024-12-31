for i in range(30):
    if i % 20 == 0:
        print("Twist")
    elif i % 15 == 0:
        pass 
    elif i % 5 == 0:
        print("fizz")
    elif i % 3 == 0:
        print("buzz")   
    else:
        print(i)   

a = int(input("Enter a number "))  
b = int(input("Enter another number "))  
if a < b:
    pass
else:
    print("A is greater than B")
