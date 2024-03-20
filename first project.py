# function for simple mathematical operation
def simple_mathematical_operations ():
    # Enter the mathematical operation as string :
    number1= input("Enter your Mathematical operations : ")
    # making sure that variable not empty :
    if not number1 :
        print(" you forgot enter your mathematical operation . Try again to continue .")
    else:    
        # use "try" and "except" concept for not stopping program ,if samething happend
        try:
            # print eval() 
            print(eval(number1))
        except:
            # A simple alert if an error occurs.
            print("your mathematical operation is not simple , please use this operation'*' or '/' or '+' or '-' ")

# call function simple_mathematical_operations()
simple_mathematical_operations()
