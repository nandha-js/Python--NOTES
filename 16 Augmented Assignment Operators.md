📘 **Topic: Augmented Assignment Operators in Python**

Used to update a variable’s value in a shorter way. ✍️  
It combines an operation and assignment together.

---

### 🧩 Operators:

| Operator | Meaning                  | Example   | Same As      |
| -------- | ------------------------ | ---------- | ------------- |
| `+=`     | Add and assign           | `x += 3`  | `x = x + 3`  |
| `-=`     | Subtract and assign      | `x -= 2`  | `x = x - 2`  |
| `*=`     | Multiply and assign      | `x *= 3`  | `x = x * 3`  |
| `/=`     | Divide and assign        | `x /= 2`  | `x = x / 2`  |
| `%=`     | Modulus and assign       | `x %= 4`  | `x = x % 4`  |
| `**=`    | Exponent and assign      | `x **= 2` | `x = x ** 2` |
| `//=`    | Floor divide and assign  | `x //= 3` | `x = x // 3` |

---

### 🧠 Example:
```python
x = 5
x += 3
print(x)   # 8

x *= 2
print(x)   # 16

x //= 3
print(x)   # 5


# 💡 Tip:
Use augmented operators to make your code shorter, cleaner, and faster, especially inside loops or repeated calculations.