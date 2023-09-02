#FizzBuzz

for i in range (1,101):
   #print(i)
   if i%3==0 and  i%5==0:
      print (i,"FizzBuzz")
   elif i%5==0:
      print(i,"Buzz")
   elif i%3==0:
      print(i, "Fizz")
   else:
       print(i)