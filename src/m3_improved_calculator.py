def add(first_param,second_param):
    return int(first_param)+int(second_param)

def subtract(first_param,second_param):
    return int(first_param)-int(second_param)
     
def multiply(first_param,second_param):
    return int(first_param)*int(second_param)
   
def divide(first_param,second_param):
    return int(first_param)/int(second_param)


###############################################################################
# DONE: 1. (4 pts)
#
#   In this module, we will improve upon the calculator that we built in the
#   Session 5 coding exercises.
#
#   First, you will need to grab the functions that you wrote for each of the
#   four main operations:
#     - add
#     - subtract
#     - multiply
#     - divide
#
#   You can simply copy and paste them into this file at the top (above this
#   _TODO_)
#
#   For this _TODO_, we will be rewriting our main() function.
#
#   First, copy your main() function from Session 5 m3 todo #2 and rename it
#   to if_calc().
#
#   Next, make these modifications
#     1. Add another prompt for the user asking which operation they want to
#        do. Make sure to show the user this key in the prompt.
#           (+) Add
#           (-) Subtract
#           (*) Multiply
#           (/) Division
#        The user should then enter one of the operators to indicate which
#        operation they want to do. Make sure you save this to a variable.
#
#     2. Now, using if statements, check which operator the user put and only
#        do the calculation that the user specified instead of all of them. If
#        the user, put something other than one of the operators, print:
#           "Invalid Operation!"
#
#   Your solution should still function just like it did in Session 5 (except
#   for the changes outlined above)   
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def  if_calc():
    print ("(+) Add")
    print("(-) Subtract")
    print("(*) Multiply")  
    print("(/) Division")
    operation=input("Please enter the operator you would like to use.")
    var1 = input("Enter input:")
    var2 = input("Enter second input:")
    if "+" == operation: 
        print("Add:", add(var1, var2))
    elif "-" == operation:
        print("Subtract:",subtract(var1, var2))
    elif "*" == operation: 
        print("Multiply:",multiply(var1, var2))
    elif "/" == operation:
        print("Divide:",divide(var1, var2))
    else : 
        print("Invalid operation.")
   
if_calc()

###############################################################################
# DONE: 2. (4 pts)
#
#   Now, do the same thing that you did in _TODO_ 1, but this time, use case
#   statements in your solution instead of if statements.
#
#   This time rename your function to case_calc(). Also, you do *not* need to
#   re-copy your operation functions. You can simply use them again.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def  case_calc():
    print ("(+) Add")
    print("(-) Subtract")
    print("(*) Multiply")  
    print("(/) Division")
    operation=input("Please enter the operator you would like to use.")
    var1 = input("Enter input:")
    var2 = input("Enter second input:")
    match operation: 
        case "+": 
            print("Add:", add(var1, var2))
        case "-":
            print("Subtract:",subtract(var1, var2))
        case "*": 
            print("Multiply:",multiply(var1, var2))
        case "/":
            print("Divide:",divide(var1, var2))
        case _ : 
            print("Invalid operation.")
   
case_calc()