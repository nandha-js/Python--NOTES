# Heading: Lexicographical Order in Python

### Syntax: string1 < string2 / string1 > string2 / string1 == string2

# 🔍 Breakdown
# Lexicographical order means dictionary order — comparing strings character by character (A → Z).
# Python compares characters using their Unicode (ASCII) values.

# 💻 Examples
print("apple" < "banana")    # Output: True (a comes before b)
print("grape" > "apple")     # Output: True
print("cat" == "cat")        # Output: True
print("Zoo" > "apple")       # Output: False (Z has smaller ASCII value than a)

# Uppercase letters come before lowercase ones
print("Apple" < "apple")     # Output: True

# Check ASCII values using ord()
print(ord('A'))  # Output: 65
print(ord('a'))  # Output: 97

# 💡 Tip
# To compare strings without case sensitivity, convert both to lowercase:
print("Apple".lower() == "apple".lower())  # Output: True

# ✅ In Short
# Strings are compared character by character using Unicode values.
# Uppercase letters come before lowercase letters.
# Use lower() to ignore case when comparing.
