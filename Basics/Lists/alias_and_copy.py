#alias

lst1 = [1,2,3,4,5,6]
lst2 = lst1
lst2[0] = 200
print(lst1, lst2)       # problem arises when changes done in lst2 reflect in lst1 also


# copy

lst3 = [4,5,6,7,8]
lst4 = lst3.copy()
lst4[0] = 100
print(lst3, lst4)