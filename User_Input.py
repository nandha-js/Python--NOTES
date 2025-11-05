"""
📘 Topic: User Input in Python

Used to take input from the user through the keyboard.

Done using the input() function.
"""
variable = input("Your message here: ")

# 
name = input("Enter your name: ")
print("Hello", name)

#👉 If you type Nandha, output → Hello Nandha

"""
🧩 Note:
By default, input() returns string type.
If you want a number, convert it:

"""
age = int(input("Enter your age: "))
print(age + 5)  # adds 5 to the number

#💡 Tip: Use int() or float() to convert input to numbers.