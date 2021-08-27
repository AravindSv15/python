try:
    x=int(input("enter a number"))
    y=int(input("enter a number"))
    z=x/y
except Exception as e:
    print("exception occured:",type(e))
    z=None
print("division is :",z)