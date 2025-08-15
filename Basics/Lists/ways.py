# 1- using square brackets

myList = [1, 2, 3.56, "Hello", True]

print(myList)


# 2- using list constructors

myList = list((1, 2, 3.56, "Hello", True))
print(myList)



# 3- range fucntion

lst1 = list(range(1, 50, 2))        # reutrns object, so we have to convert it into a list
print(lst1)



# 4- List Comprehention
"""
item - i
iterable - range(0,11)
condition(optional) - i%2==0
"""

squares = [i**2 for i in range(0,11) if i%2==0]
print("Squares: ",squares)





# updatation

lst = [1,2,3,4,5,6]
lst[0: 3] = 10, 20, 30
lst[5] = "Hello"
print(lst)


#concatiation

print(myList + lst)