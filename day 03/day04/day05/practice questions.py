# n = int(input("enter n : "))
# sum = 0
# i = 0
# while i <= n:
#     sum = (sum + i)
#     i += 1
# print(sum)
n = int(input("enter n: "))
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)    