#append - adds element in the last position

lst1 = [1,2,3,4]
lst1.append(5)
print(lst1)


#extend - adds the argument passed list elements in the prev. list

a = [1,2,3,4]
b = [5,6,7,8]
a.extend(b)
print(a)


#insert method - inserts an element at a specific position in a list

a1 = [1,2,3,4,5]
a1.insert(1, "Hello")       # (position, data)
print(a1)


#remove method - deletes the data passed into the method

a1.remove(3)
print(a1)


# pop method - pops/ deteles a particular element, but here the index number has to be passed

popped = a1.pop(0)                  # returns the element that is popped
print("Element popped: ",popped)        
print(a1)


# clear method - clears everything in a list and returns an empty list

a2 = [3,4,5,6,7]
a2.clear()
print(a2)


# index method - returns the index number of the passed element if present int he list

a3 = [2,3,4,5,6,7]
index = a3.index(5)
print("Index: ",index)


# count method - returns the frequency of a particular element in a list

a4 = [1,2,2,2,2,2,3,2,1,2,4,5,6,"hello", "bye"]
counter = a4.count(2)
print("Frequency: ",counter)


# sort method - it sorts the list in assending order

a5 = [1,2,2,2,2,2,3,2,1,2,4,5,6,]
a5.sort()                               # uses tim sort
print(a5)       



# reverse method - it reverses the element order of the list

a4.reverse()
print(a4)


# copy method - it copies the values from one list to the other list

lst3 = [4,5,6,7,8]
lst4 = lst3.copy()
lst4[0] = 100
print(lst3, lst4)