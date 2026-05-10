student_scores = [180, 124, 165, 173, 189, 169, 146]

# Py has a sum() func, which takes any iterable data type
# and returns the addition of each of the number in the iterables
"""
total_exam_score = sum(student_scores)
print(total_exam_score)
"""

# it can also be done manually
'''
sum = 0

for i in student_scores:
    sum += i

print(sum)
'''
# Challenge, Try and replicate max() functionality
# -- It allows us to find the largest number in list

# student_scores = [180, 124, 165, 173, 189, 169, 146]
max_num = 0
for num in student_scores:
    print(num)
    if num > max_num:
        max_num = num


print(f"This is the largest number {max_num}")

min_num = max_num
for num in student_scores:
    if num < min_num:
        min_num = num
print(min_num)
