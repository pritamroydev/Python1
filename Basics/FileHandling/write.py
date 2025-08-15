"""
file.write(content)
"""

file = open(r"C:\Users\user\Desktop\Lang\Python1\Basics\FileHandling\files2.txt", "w")
content = input("Enter your data: ")
file.write(content)
print("Written Successfully")
file.close()