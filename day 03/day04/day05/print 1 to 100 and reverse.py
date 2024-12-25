# i = 1
# while i<=100:
#  print(i)
#  i += 1
#  now print 100 to 1
# i = 100
# while i >=1:
#   print(i)
#   i -= 1
#table of n
# n = int(input("enter number")) 
# i = 1
# while i<=10:
#     print(i*n)
#     i+=1
# print squares of numbers
# i = 1
# while i<=10:
#     print(i*i)
#     i+=1
#SEARCH FOR A NO. x IN THE LOOP
x = int(input("enter the no."))
nums = (1,4,9,16,25,36,49,64,81,100)
i = 0
while i< len(nums):
    if (nums[i]==x):
        print("found at idx" , i)
    elif nums[i]=!x:
        print("number is not in loop")