#Sort using For LOOP/break

scores_list = [78,65,89,55,45,82,23,47,34,67,40,99]
x=0
#print(len(a))
for x in range(0,len(scores_list)-1):
  for n in range(0,len(scores_list)): 
     #print(n)
     if scores_list[n] < scores_list[n+1]:
        x = scores_list[n]
        scores_list[n]=scores_list[n+1]
        scores_list[n+1]=x
     #print(a)
     if n+1 == len(scores_list)-1:
        #print("inside break",n)
        break
print("The highest score is :", scores_list[0])    