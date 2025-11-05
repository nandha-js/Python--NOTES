"""
📘 Topic: Logical Operators in Python

Used to combine or compare conditions.

Always return True or False. ✅❌

🧩 Logical Operators:

| Operator | Meaning                               | Example                | Result |
| -------- | ------------------------------------- | ---------------------- | ------ |
| `and`    | True if **both** conditions are true  | `(5 > 2) and (10 > 5)` | `True` |
| `or`     | True if **any one** condition is true | `(5 > 10) or (10 > 5)` | `True` |
| `not`    | Reverses the result                   | `not(5 > 10)`          | `True` |



"""
x = 10
y = 5

print(x > 5 and y < 10)   # True (both true)
print(x < 5 or y < 10)    # True (one true)
print(not(x == 10))       # False (because x == 10 is True)

#💡 Tip:Logical operators are often used in if statements for multiple conditions.

#Truth Table for Logical Operators

"""
| A     | B     | `A and B` | `A or B` | `not A` |
| ----- | ----- | --------- | -------- | ------- |
| True  | True  | True      | True     | False   |
| True  | False | False     | True     | False   |
| False | True  | False     | True     | True    |
| False | False | False     | False    | True    |

"""
A = True
B = False

print(A and B)   # False
print(A or B)    # True
print(not A)     # False


"""
💡 Tips:

and → both must be True

or → at least one must be True

not → flips True ↔ False
"""