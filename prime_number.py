#Prime number check

def prime_checker(number):
    is_prime="True"
    for i in range(2,number):
        if number%i == 0:
            is_prime="False"
            break
    if is_prime == "True":
         print(number,":", "Is a prime ")
    else:
         print(number,":", "Not a prime ")
        
#main        
var_number = int(input("Enter a number to check:"))
prime_checker(number=var_number)