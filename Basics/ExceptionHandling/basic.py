"""
if 1==1
    print("Hello")                        # compiletime error

"""

"""
print ( 2 % 0)                      # runtime error

"""


"""
a = int(input("Enter 1st number: "))                # when the O/P is not as desired, it is called Logical error
b = int(input("ENter 2nd number: "))
print(f'Sum: {a*b}')


"""





# exception handling
"""
try:
    num = int(input("Enter a number: "))
    result = 10/num
    print(f'result: {result}')

except ZeroDivisionError:
    print("You can't divide with 0...")

except ValueError:
    print("Please exter a number...")


"""

#nested try-except blocks

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    try:
        result = num1/num2
        print(f'result= {result}')
    
    except ZeroDivisionError:
        print("You can't divide by 0...")

except ValueError:
    print("Enter valid input...")
