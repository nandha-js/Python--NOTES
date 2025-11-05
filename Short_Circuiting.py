"""
📘 Topic: Short-Circuiting in Python

Short-circuiting means Python stops checking conditions early when the result is already known. ⚡

It happens with and and or operators.

"""


#🔹 and Operator

"""

If the first condition is False, Python won’t check the second one.

Because the final result will always be False.

"""
print(False and True)   # Stops early → False

x = 0
print(x != 0 and (10 / x > 1))  # No error, second part not checked

#🔹 or Operato

"""
If the first condition is True, Python won’t check the second one.

Because the final result will always be True.
"""
print(True or False)   # Stops early → True

x = 10
print(x > 5 or (10 / 0))  # No error, second part not checked


#💡 Tip:Short-circuiting helps make your code faster and safer, especially when the second condition might cause an error.

#💡 Easy to remember:    and → stops at False ""<          >""     or → stops at True