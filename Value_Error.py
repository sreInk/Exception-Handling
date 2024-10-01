try:
    num = int(input("Enter Number"))
    print("the number is",num)
except ValueError as ex:
    print("Ans is",ex) 