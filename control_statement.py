cha = input("enter any character ")
if len(cha) !=1:
    print("print only single character ")
else:
    if cha.isupper():
        print("upper case")
    elif cha.islower():
        print("lower case")
    elif cha.isdigit():
        print("digit")
    else:
        print("special character")



