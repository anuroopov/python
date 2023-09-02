#Sum of all even numbers upto 100:

total=0
for i in range (2,101,2):
    #print(i)
    total=total+i
print (total)

total=0
for i in range (1,101):
    #print(i)
	if i%2==0:
    total=total+i
print (total)