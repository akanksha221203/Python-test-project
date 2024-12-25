a = int(input("select a no. between 1 and 50 :"))
if(a>=18):
    print("to high")
    b = int(input("select a no. less then your no." ))
    if(b==17):
        print("you won")
    else:
        print("you lose!")

if(a<=16):
    print("to low")
    c = int(input("select a no. greater then your no."))
    if(c==17):
          print("you won")
    else:
          print("you lose")
          
          
