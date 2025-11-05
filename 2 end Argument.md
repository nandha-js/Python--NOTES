# Heading: end Argument in print() Function

### Syntax: print(..., end='character')

# 🔍 Breakdown
# object : The value(s) you want to print (text, variable, number, etc.)
# end    : Character printed at the end of the output (default = '\n' for new line)

# 💻 Examples
print("Hello", end=" ")
print("World")      # Output: Hello World

print("A", end="-")
print("B")          # Output: A-B

print("1", end="")
print("2")          # Output: 12

# 💡 Tip
# Use end="" to keep output on the same line.
# You can also use spaces, dashes, or any character to separate outputs.

# ✅ In Short
# The 'end' argument in print() controls what is printed at the end of a line.
# By default it moves to a new line, but you can customize it as needed.
