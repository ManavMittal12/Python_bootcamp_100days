# Mathematical Operations
print("my age: " + str(2))  # <--- Concatenation
print(123 + 126) # <--- Addition
print(7 - 3) # <--- Subtraction
print(3 * 2) # <--- Multiple
print(6 / 3) # <-- Division -- It's also called Implicit type casting
# Because it converts the final result to float implicitly
print(6 // 3) # <--- Integer Division
print(6 ** 2) # <-- To put a value on power of another
print(6 % 4) # <--- modulus, will return remainer

# Be careful about when you have more mathematical operation to same
# line of code. There's a certain level of priority
# The rule that is followed is called "PEMDAS",
# Can also consider "PEMDASLR"

# 1) Parenthesis
# 2) Exponents
# 3) Multiplication & Division
# 4) Addition & Subtraction
# 5) Left to Right for equal precedence.

print(3 * ((3 + (3 / 3)) - 3))
# Answer : 7.0


## Challenge 2
# Make changes such that the output was 3.0
print(3 * ((3 + (3 / 3)) - 3))
