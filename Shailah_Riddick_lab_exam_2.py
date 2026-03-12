# Write a Python function that:
# Accepts a list of student names and grades (students, grades) as input.

# Validates:
# Grades must be integers 0–100 (raise InvalidGradeException, a custom exception).
# Names must be unique (raise DuplicateNameException, a custom exception).

# Computes and Visualize Statistics with a Pie Chart:
#  Find and print the mean and median score. You can use the python native statistics library https://docs.python.org/3/library/statistics.html Or numpy
#  Find and print pass/fail counts (≥70 passes).
# Create a pie chart using matplotlib based on pass/fail count. (Refer to slide #4 for a sample chart)


import matplotlib.pyplot as plt
import numpy as np
from statistics import mean, median

class InvalidGradeException(Exception):
    pass

class DuplicateNameException(Exception):
    pass

def analyze_student_performance(students, grades):
    # Create a dictionary to track input names and grades. Then validate inputs.
    if len(students) != len(set(students)):
        raise DuplicateNameException("Duplicate student names are not allowed.")

    for g in grades:
        if not isinstance(g, int) or g < 0 or g > 100:
            raise InvalidGradeException("Grades must be integers between 0 and 100.")

    # Compute statistics
    avg = mean(grades)
    med = median(grades)

    print(f"Mean score: {avg}")
    print(f"Median score: {med}")

    passes = sum(1 for g in grades if g >= 70)
    fails = len(grades) - passes

    print(f"Passes: {passes}, Fails: {fails}")

    # Create pie chart
    labels = ['Pass', 'Fail']
    sizes = [passes, fails]

    plt.figure(figsize=(9, 9))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Pass/Fail Distribution")
    plt.show()

# === Example usage and test cases. Do not modify the code below this line ===
# Test case 1:
students = ['a', 'b', 'c']
grades = [90, 100, 40]
analyze_student_performance(students, grades)

# Test case 2: (InvalidGradeException should be raised)
students = ['a', 'b', 'c']
grades = [90, 70, 110]
analyze_student_performance(students, grades)

# Test case 3: (DuplicateNameException should be raised)
students = ['a', 'b', 'a']
grades = [90, 70, 100]
analyze_student_performance(students, grades)
