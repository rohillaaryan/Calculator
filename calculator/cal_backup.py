list_history = []

def history(list_history, num1, num2, operator, result): # this history gives us a list of programs that were successful, it's just calculation history & not a debugging/logging system
    list_history.append(f"{num1} {operator} {num2} = {result:.4f}")
    print(list_history)

def convert(num):
    try:
        num = float(num) #try runs the entire indented block underneath it and if error occurs it goes to except
        return num
    except ValueError:
        print("value error") #except does what we tell it to if try fails #here we tell except to work if the error type is only value error. In any other error the code will stop and we will have an error
        #exit() #it just stops the program

def calculator(num1, num2, operator):  #def is used to define a fxn it is called later when we need it
    if operator not in ("+","-","*","/","%"): #in keyword checks if the operator is in the operators mentioned and not in is opposite of it
        return("invalid operator")
    elif operator=='+':
        return(num1+num2)
    elif operator == '-':
        return(num1-num2)
    elif operator == '*':
        return(num1*num2)
    elif operator == '/':
        try:
            return(num1/num2)
        except ZeroDivisionError:
            return("ZeroDivisionError")
    elif operator == '%':
        try:
            return(num1%num2)
        except ZeroDivisionError:
            return("ZeroDivisionError")

def op(operator):
    while operator not in ('+','-','*','/','%'):
        operator=input("enter operator (+,-,*,/,%) : ")
    return operator

def start_calculator():

    num1 = None
    while num1 is None:
        num1=(input("enter first no. : "))
        num1 = convert(num1)

    temp_operator = input("enter operator (+,-,*,/,%) : ")   
    operator = op(temp_operator) 

    num2 = None
    while num2 is None:
        num2=(input("enter second no. : "))
        num2 = convert(num2)

    result = calculator(num1, num2, operator) #here we called our fxn as we needed it
    print(result)

    if type(result) == float: #One thing to think about later: type(result) == float is a fairly specific check. Your calculator currently produces floats because convert() converts both inputs to floats, but think about what you're really trying to check: "Is this a successful calculation?" rather than merely "Is this specifically a float?"
        history(list_history, num1, num2, operator, result)

def check(restart):
    while restart in 'y' or restart not in ('n'): #i don't understand how this line works but it works // while restart == 'y' or restart not in ('y' , 'n'): // earlier i was using this
        if restart == 'y':
            start_calculator()

            restart = input("start the calculator (y or n) : ").lower()
        else:
            restart = input("start the calculator (y or n) : ").lower()

def start(restart):
    while restart not in ('y' , 'n'):
        restart = input("start the calculator (y or n) : ").lower()
    check(restart)
    
restart = input("start the calculator (y or n) : ").lower()
start(restart)
