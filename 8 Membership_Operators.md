# Heading: Membership Operators in Python

### Syntax: value in sequence / value not in sequence

# 🔍 Breakdown
# Used to check if a value is present in a sequence (string, list, tuple, etc.).
# Returns True or False ✅❌

# 💻 Common Membership Operators
# | Operator | Meaning                                | Example              | Result |
# | -------- | -------------------------------------- | -------------------- | ------ |
# | in       | Returns True if value is found         | 'a' in 'apple'       | True   |
# | not in   | Returns True if value is **not** found | 'x' not in 'apple'   | True   |

# 💻 Examples
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)      # Output: True
print("grape" not in fruits)  # Output: True

name = "Nandha"
print('a' in name)            # Output: True
print('z' not in name)        # Output: True

# 💡 Tip
# Useful for checking if an item exists before performing an action.

# ✅ In Short
# 'in' and 'not in' can be used with if, while, for, print(), or any expression that needs a True/False result.
