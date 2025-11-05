"""
📘 Topic: Data Types in Python

Data types tell what kind of value a variable holds.

Python decides the type automatically.

🧩 Basic Data Types:
| Type    | Example                         | Description                          |
| ------- | ------------------------------- | ------------------------------------ |
| `int`   | `10`                            | Whole numbers                        |
| `float` | `3.14`                          | Decimal numbers                      |
| `str`   | `"Hello"`                       | Text (string)                        |
| `bool`  | `True`, `False`                 | True/False values                    |
| `list`  | `[1, 2, 3]`                     | Ordered, changeable collection       |
| `tuple` | `(1, 2, 3)`                     | Ordered, **unchangeable** collection |
| `set`   | `{1, 2, 3}`                     | Unordered, unique items              |
| `dict`  | `{"name": "Nandha", "age": 22}` | Key-value pairs                      |

"""

x = 10          # int
y = 3.14        # float
name = "Nandha" # str
is_happy = True # bool


#💡 Use type() to check the data type:
print(type(x))  # 👉 <class 'int'>

