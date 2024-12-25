#break is to terminate the loop.basically end of the loop.
#continue is used to skip the some elements.
# i = 0
# while i <= 10:
#     if(i==3):
#         break
#     print(i)
#     i += 1
i = 1
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1
