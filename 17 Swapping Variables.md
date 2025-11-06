📘 **Topic: Swapping Variables in Python**

Swapping means exchanging the values of two variables. 🔁  
In Python, it can be done easily **without using a temporary variable**.

---

### 🧩 Example 1 — Using a Temporary Variable
x = 10
y = 20

temp = x
x = y
y = temp

print(x, y)   # 👉 Output: 20 10

---

### 🧩 Example 2 — Pythonic Way (Without temp)
x = 10
y = 20

x, y = y, x

print(x, y)   # 👉 Output: 20 10

---

### 🧩 Example 3 — Swap More Than Two
a, b, c = 1, 2, 3
a, b, c = c, a, b

print(a, b, c)   # 👉 Output: 3 1 2

---

💡 **Tip:**  
Python allows multiple assignments in one line — making swaps **clean, fast, and elegant**.
