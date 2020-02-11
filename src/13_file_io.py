"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
import os
os.chdir(f"{os.getcwd()}/src")

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# f = open('foo.txt')

# print(f.read())
# print(f.close())
with open('foo.txt', 'r') as f:
     read_data = f.read()
     print(read_data)

print(f.closed)
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open('bar.txt', 'w') as b:
     read_data = b.write("This is a test\n")
     read_data = b.write("I'm starting to understand Python now!")
     read_data = b.write("Hopefully it'll stay like this")
     print(read_data)

with open('bar.txt', 'r') as b:
    bar = b.read()
    print(bar)
    
print(f.closed)