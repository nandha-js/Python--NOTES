"""
📘 Topic: Identity Operators in Python

Used to check if two variables refer to the same object in memory.

Returns True or False. ✅❌


| Operator | Meaning                                        | Example      | Result       |
| -------- | ---------------------------------------------- | ------------ | ------------ |
| `is`     | True if both variables are the **same object** | `a is b`     | True / False |
| `is not` | True if they are **different objects**         | `a is not b` | True / False |


"""
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)       # True  (same object)
print(x is z)       # False (different objects)
print(x is not z)   # True

"""
💡 Tip:

is checks memory location, not just value.

To compare values, use ==.
"""
print(x == z)   # True (same values)

