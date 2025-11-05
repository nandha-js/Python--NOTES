# Heading: Print Function in Python

### Syntax: print()

# 🔍 Breakdown
# object : The value(s) you want to print (text, variable, number, etc.)
# sep    : Separator between multiple values (default = space ' ')
# end    : Character printed at the end (default = newline '\n')

# 💻 Examples
print("Hello, World!")                    # Simple text
print("Python", "is", "fun")              # Prints with spaces
print("Python", "is", "fun", sep='-')     # Custom separator
print("Hello", end=' ')                   # Change end character
print("World!")                           # Output: Hello World!

name = "Nandha"
print(f"My name is {name}")               # Using f-string formatting

# 💡 Tip
# Combine text and variables easily using f-strings.
# Use 'sep' and 'end' to customize output format.

# ✅ In Short
# The print() function displays output on the screen.
# You can customize separators and line endings as needed.
