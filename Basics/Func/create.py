def greet(name):
    greet = f"Hello {name}"
    return greet

print(greet("Pritam"))
print(type(greet("Pritam")))



def add(a, b):          # a, b are parameters
    return a+b

print((add(5, 6)))      # 5, 6 are arguments



def greet1(name="Pritam", city="Andal"):
    print(f"Welcome {name} to {city}")


# positional arguments
greet1("mumbai", "raju")


#keyword arguments
greet1(city="mumbai", name="Raju")


#default arguments
greet1()