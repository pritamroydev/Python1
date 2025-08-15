"""
with open("filePath", "mode") as fileName:
"""

with open(r"C:\Users\user\Desktop\Lang\Python1\Basics\FileHandling\data.txt", "w") as file:
    content = input("Enter content to write: ")
    file.write(content)
    print("Saved!")