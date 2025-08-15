"""
in - True/ False
not in - opposite
"""


myList = [1, 2, 3.56, "Hello", True]
check = int(input("Enter a number: "))
if check in myList:
    print("Found")
else:
    print("Not found")