profile = {
    "Name": "Ram", "Age": 44, "Salary": 25000.00, 8317897731: "Pritam"
}

# get method    - returns the value of the passed key

print(profile.get("Name"))
print(profile.get(8317897731))

print(profile.get("Surname", "Not Found"))      # if that particular keyt is not found, they it will display this message



# keys method       - returns the keys available in the dictionary

print(list(profile.keys()))


# value method      - returns the values available in the dictionary

print(list(profile.values()))


# items method      - returns both the keys-value pair available in the dictionary

print(list(profile.items()))
print(dict(profile.items()))
print()



# pop method        - pops the passed key, returns the popped value

pop = profile.pop("Age")
print("Popped value", pop)

pop = profile.pop("Age_2", "Not Found")
print("Popped value", pop)

print(profile)
print()



# pop item          - pops the last item by default

profile1 = {
    "Name": "Shyam", "Age": 44, "Salary": 25000.00
}
print(profile1)
pop1 = profile1.popitem()
print("Popped Item:",pop1)
print(profile1)



# clear method      - clears the whole dict

print(profile1)
profile1.clear()
print(profile1)





# dict comprehensions

squares = {
    x: x**2 for x in range(1,11) if x%2==0
}
print(squares)