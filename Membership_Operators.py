"""📘 Topic: Membership Operators in Python

Used to check if a value is present in a sequence (like a string, list, tuple, etc.).

Returns True or False. ✅❌

🧩 Operators:

| Operator | Meaning                                | Example              | Result |
| -------- | -------------------------------------- | -------------------- | ------ |
| `in`     | Returns True if value is found         | `'a' in 'apple'`     | `True` |
| `not in` | Returns True if value is **not** found | `'x' not in 'apple'` | `True` |


"""

fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)      # True
print("grape" not in fruits)  # True

name = "Nandha"
print('a' in name)            # True
print('z' not in name)        # True

#💡 Tip: Useful for checking if an item exists before performing an action.

"""
💡 Summary:
✅ You can use in / not in with:

if, while, for

print()

or any expression that needs a True/False result.

Would you like the next topic — identity operators (is, is not)?

"""