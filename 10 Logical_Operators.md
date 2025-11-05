# Heading: Logical Operators in Python

### Syntax: condition1 and/or/not condition2

# 🔍 Breakdown
# Used to combine or compare multiple conditions.
# Always returns True or False ✅❌

# 💻 Common Logical Operators
# | Operator | Meaning                               | Example                | Result |
# | -------- | ------------------------------------- | ---------------------- | ------ |
# | and      | True if **both** conditions are true  | (5 > 2) and (10 > 5)   | True   |
# | or       | True if **any one** condition is true | (5 > 10) or (10 > 5)   | True   |
# | not      | Reverses the result                   | not(5 > 10)            | True   |

# 💻 Examples
x = 10
y = 5

print(x > 5 and y < 10)   # Output: True (both true)
print(x < 5 or y < 10)    # Output: True (one true)
print(not(x == 10))       # Output: False (x == 10 is True)

# Truth Table
# | A     | B     | A and B | A or B | not A |
# | ----- | ----- | ------- | ------ | ------ |
# | True  | True  | True    | True   | False  |
# | True  | False | False   | True   | False  |
# | False | True  | False   | True   | True   |
# | False | False | False   | False  | True   |

A = True
B = False

print(A and B)   # Output: False
print(A or B)    # Output: True
print(not A)     # Output: False

# 💡 Tip
# and → both conditions must be True
# or  → at least one condition must be True
# not → flips True ↔ False

# ✅ In Short
# Logical operators combine conditions and always return a Boolean result.
