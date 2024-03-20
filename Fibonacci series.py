# this function for call Fibonacci series like a list.
def Fibonacci_series ():
    try:
        # this "while loop" for repeat if variable "number" is a negative number. 
        while True :
            # not for users
            print("note : you need to enter a positive natural number or this function not working .")
            # save the input value in variable hase name "number".
            number= int(input("Enter your number for convert it a Fibonacci series : "))
            # the if condition to check if number variable is a nigative number.
            if number < 0:
                #print error
                print("your number is negative try again")
            else:
                # break the loop if number >= 0.
                break
        # Create an empty list to store the Fibonacci series
        num=[] 
        # Loop to verify the Fibonacci series   
        for i in range(number+1):
            #0 and 1 are the fundamental numbers in the Fibonacci series
            if i == 0 or i == 1 :
                # add to num list
                num.append(i)
            else:
                #num[-1] The last number in the list 
                #num[-2] The penultimate number in the list
                a=num[-1]+num[-2]
                #add the sum in "num" list
                num.append(a)

        return num
    except  :
        #print error if something wrong
        print("your input is incorrect try again")

