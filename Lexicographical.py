"""
📘 Topic: Lexicographical Order in Python

Lexicographical order means dictionary order — comparing strings character by character (A → Z).

Python compares characters using their Unicode (ASCII) values.

🧩 Examples:


"""

print("apple" < "banana")    # True (a comes before b)
print("grape" > "apple")     # True
print("cat" == "cat")        # True
print("Zoo" > "apple")       # False (Z has smaller ASCII value than a)

#✨ Notes: Uppercase letters come before lowercase ones.

print("Apple" < "apple")   # True

#You can check the ASCII value using ord():

print(ord('A'))  # 65
print(ord('a'))  # 97

#💡 Tip:To compare strings without case sensitivity, convert both to lowercase:

print("Apple".lower() == "apple".lower())  # True

