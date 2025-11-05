"""
📘 Topic: Bitwise Operators in Python

Bitwise operators work on binary (bits) of numbers — 0s and 1s.

They compare or shift bits directly. ⚙️

🧩 List of Bitwise Operators:

| Operator | Name        | Example  | Result (in binary)   | Output |       |              |     |
| -------- | ----------- | -------- | -------------------- | ------ | ----- | ------------ | --- |
| `&`      | AND         | `5 & 3`  | `0101 & 0011 = 0001` | `1`    |       |              |     |
| `        | `           | OR       | `5                   | 3`     | `0101 | 0011 = 0111` | `7` |
| `^`      | XOR         | `5 ^ 3`  | `0101 ^ 0011 = 0110` | `6`    |       |              |     |
| `~`      | NOT         | `~5`     | flips all bits       | `-6`   |       |              |     |
| `<<`     | Left Shift  | `5 << 1` | `0101 → 1010`        | `10`   |       |              |     |
| `>>`     | Right Shift | `5 >> 1` | `0101 → 0010`        | `2`    |       |              |     |


"""
a = 5   # 0101
b = 3   # 0011

print(a & b)   # 1
print(a | b)   # 7
print(a ^ b)   # 6
print(~a)      # -6
print(a << 1)  # 10
print(a >> 1)  # 2

#💡 Tip:Bitwise operators are used in low-level operations, like encryption, masks, or performance-heavy logic.
