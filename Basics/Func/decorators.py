def myDecorator(func):
    def wrapper():
        print("Something is happening before the func")
        func()
        print("Something is happening after the func")
    return wrapper

@myDecorator
def sayHello():
    print("Hello")

sayHello()



"""
Explanation:

🎁 Your Analogy     vs  Code:

        Analogy	                                            What It Means in Code

You are the decorator	                        myDecorator function
Someone calls you @myDecorator	                Python applies myDecorator to the function below it
The gift is the function below	                e.g., sayHello() — this is passed as func
You wrap it with wrapping paper	                You define a wrapper() that adds behavior around func()
You return the wrapped gift	                    You return the wrapper function (not the original)
The caller now receives a new gift	            sayHello() now points to wrapper() instead of original

"""