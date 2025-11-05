# Heading: Identity Operators in Python

### Syntax: a is b / a is not b

# 🔍 Breakdown
# Used to check if two variables refer to the **same object in memory**.
# Returns True or False ✅❌

# 💻 Common Identity Operators
# | Operator  | Meaning                                     | Example      | Result       |
# | --------- | ------------------------------------------- | ------------ | ------------ |
# | is        | True if both variables are the **same object** | a is b     | True / False |
# | is not    | True if variables are **different objects**   | a is not b | True / False |

# 💻 Examples
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)       # Output: True  (same object)
print(x is z)       # Output: False (different objects)
print(x is not z)   # Output: True

# Compare values, not objects
print(x == z)       # Output: True (same values)

# 💡 Tip
# 'is' checks memory location, not just value.
# Use '==' to compare values.

# ✅ In Short
# Identity operators check if two variables point to the same object in memory.
