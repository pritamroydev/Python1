try:
    file = open(r'C:\Users\user\Desktop\Lang\Python1\ExceptionHandling\errors.txt','r')
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File Not Found...")

finally:
    file.close()
    print("\n\nFile Operation Completed...")