# File Write Example

file = open("sample.txt", "w")

file.write("Hello, this is my first file in Python!")

file.close()


# File Read Example

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()