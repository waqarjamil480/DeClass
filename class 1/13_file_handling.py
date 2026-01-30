file = open("file.txt", "r")  # modes: 'r', 'w', 'a', 'x', 'b'
file.close()

# file open using with
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# writing to a file
with open("file.txt", "w") as file:
    file.write("Hello, world!")


# reading line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())

# Write to file
with open("data.txt", "w") as f:
    f.write("Python is great!\n")
    f.write("File handling is easy.")

# Read from file
with open("data.txt", "r") as f:
    print(f.read())


f.read()         # All content as a single string  
f.readline()     # One line at a time  
f.readlines()    # List of lines
