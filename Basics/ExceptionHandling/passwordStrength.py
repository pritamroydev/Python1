# checking password strength

def checkPassword(password):
    if len(password) < 8:
        raise Exception("Error: Password must be >= 8 characters")
    
    print("Password is strong")


try:
    password = input("Enter your password: ")
    checkPassword(password)

except Exception as e:
    print(e)