a = int(input("Number 1: "))
b = int(input("Number 2: "))

while a != b:
    if a>b:
        a = a-b
    else:
        b = b-a
        
print("NOD:", a)