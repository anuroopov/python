#calculator - recursion 
from art import logo

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2


def divide(n1,n2):
    return n1/n2


# create a dictionary called operations
# keys = + - * /
# values = add subtract multiply divide

dict_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = int(input("whts the first number?:"))
    num2 = int(input("whts the second number?:"))

    for symbol in dict_operations:
        print(symbol,sep="\n")
    
    operation_symbol = input("Pick an operation from the line above: ")

    function = dict_operations[operation_symbol] 
    answer= function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    #var_continue=input(f"Type 'y' to continue calculating with {answer}, or 'n' to exit")
    var_continue="y"
    #answer2=answer
    while var_continue=="y":
        var_continue=input(f"Type 'y' to continue calculating with {answer}, or 'n' to exit")
        if var_continue == "n":
            calculator()
        else: 
            operation_symbol = input("Pick an operation from the line above: ")
            num3 = int(input("whts the next number?:"))
            function = dict_operations[operation_symbol] 
            answer2=answer
            answer= function(answer2,num3)
   
            print(f"{answer2} {operation_symbol} {num3} = {answer}")
        
calculator()