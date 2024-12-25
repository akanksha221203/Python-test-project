a = int(input("enter 1st no. "))
b = int(input("enter 2nd no. "))
c = int(input("enter 3rd no. "))
if((a>b and b>c) or (a>c and c>b)):
    print("a is greatest")
elif((b>a and a>c) or (b>c and c>a)):
    print("b is greatest")
elif((c>a and a>b) or (c>b and b>a)):
    print("c is greatest")
elif a==b==c:
    print("all are equal")
elif a==b :
    if(a>c):
        print("a and b are equal and greatest")
    else:
        print("c is greatest")
elif b==c:
    if(b>a):
        print("b and c are equal and greatest.")
    else:
        print("a is greatest.")
elif a==c:
    if(a>b):
        print("a and c are equal and greatest.")
    else:
        print("b is greatest")
