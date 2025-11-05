# Heading: Bitwise Operators in Python

### Syntax: a <operator> b

# 🔍 Breakdown
# Bitwise operators work on the binary (bits) of numbers — 0s and 1s.
# They compare or shift bits directly ⚙️

# 💻 Common Bitwise Operators
# | Operator | Name        | Example  | Result (binary)     | Output |
# | -------- | ----------- | -------- | ------------------ | ------ |
# | &        | AND         | 5 & 3    | 0101 & 0011 = 0001 | 1      |
# | \|       | OR          | 5 \| 3   | 0101 \| 0011 = 0111 | 7     |
# | ^        | XOR         | 5 ^ 3    | 0101 ^ 0011 = 0110 | 6      |
# | ~        | NOT         | ~5       | flips all bits      | -6     |
# | <<       | Left Shift  | 5 << 1   | 0101 → 1010         | 10     |
# | >>       | Right Shift | 5 >> 1   | 0101 → 0010         | 2      |

# 💻 Examples
a = 5   # 0101
b = 3   # 0011

print(a & b)   # Output: 1
print(a | b)   # Output: 7
print(a ^ b)   # Output: 6
print(~a)      # Output: -6
print(a << 1)  # Output: 10
print(a >> 1)  # Output: 2

# 💡 Tip
# Bitwise operators are useful in low-level operations like encryption, masks, or performance-heavy logic.

# ✅ In Short
# Bitwise operators manipulate individual bits of numbers directly.
