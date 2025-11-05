"""
📘 Topic: print() Function in Python

Purpose: Used to display output on the screen.

Type: It’s a built-in function (not a statement).


"""

print(object, sep=' ', end='\n')

"""
object: What you want to print (text, variable, number, etc.)

sep: Separator between multiple values (default = space ' ')

end: What to print at the end (default = newline \n)

"""

print("Hello, World!")                    # Simple text
print("Python", "is", "fun")              # Prints with spaces
print("Python", "is", "fun", sep='-')     # Custom separator
print("Hello", end=' ')                   # Change end character
print("World!")                           # Output: Hello World!

#✨ Tip:
# You can combine text and variables easily:

name = "Nandha"
print(f"My name is {name}")   # f-string formatting

