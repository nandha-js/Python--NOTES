# Heading: Short-Circuiting in Python

### Syntax: condition1 and/or condition2

# 🔍 Breakdown
# Short-circuiting means Python stops checking conditions early when the result is already known ⚡
# Happens with `and` and `or` operators.

# 💻 Examples

# 🔹 and Operator
# If the first condition is False, Python won’t check the second one
print(False and True)   # Output: False (stops early)

x = 0
print(x != 0 and (10 / x > 1))  # Output: False (second part not checked, no error)

# 🔹 or Operator
# If the first condition is True, Python won’t check the second one
print(True or False)    # Output: True (stops early)

x = 10
print(x > 5 or (10 / 0))  # Output: True (second part not checked, no error)

# 💡 Tip
# Short-circuiting makes code faster and safer, especially if the second condition could cause an error.

# 💡 Easy to remember
# and → stops at False
# or  → stops at True

# ✅ In Short
# Python stops evaluating conditions as soon as the final result is determined.
