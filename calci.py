print("Welcome to faulty calci devloped by Jaydeep Singh ")
while(True):
    inp1=int(input("Enter number 1 : "))
    inp2=int(input("Enter number 2: "))
    exp=str(input("enter operator : "))
    
    if inp1==45 and inp2==3 and exp== '*':
        print("555")
        continue
    elif inp1==56 and inp2==9 and exp== '+':
        print("77")
        continue
    if inp1==56 and inp2==6 and exp== '/':
        print("4")
        continue
    elif exp == '*':
        print(inp1*inp2)
        continue
    elif exp == '+':
        print(inp1+inp2)
        continue
    elif exp == '/':
        print(inp1/inp2)
        continue
    elif exp == '-':
        print(inp1-inp2)
        continue
    elif exp == '%':
        print(inp1%inp2)
        continue
    else:
        print("some error")
        break
    
     