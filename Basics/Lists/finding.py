#max & min

lst1 = [1,54,87,6,2,1,5,48,9,9,8,7,9,41,1]
print("Max: ",max(lst1))
print("Min: ",min(lst1))


# common element

a1 = [1,2,3]
a2 = [2,3,4,5]

s1 = set(a1)            # builds an unordered collection of *unique elements*
s2 = set(a2)

s3 = s1.intersection(s2)        # returns intersection(common element) between 2 sets

print(list(s3))

