# Part 2 (Continuation)
def get_average_grade(grades_tuple):
    """Takes a tuple of numeric grades and returns the average. Ha ndles empty tuples."""
    try:
        if not grades_tuple:
            raise ZeroDivisionError("Tuple is empty.")
        return sum(grades_tuple) / len(grades_tuple)
    except ZeroDivisionError:
        print("Warning: Cannot calculate average for an empty grade tuple.")
        return None
# dictionary where keys are course names (e.g., “Math”, “Science”, “History”) and values are tuples of grades.
course_grades = {
    "Math": (85,90,92,88),
    "Science": (78, 82, 80),
    "History": (95, 91, 98, 92),
    "Art": () #Intentionaly empty edge case to the test excemtion/None handling
    }
print("--- Course Average Processing ---")
for course, grades in course_grades.items():
    avg = get_average_grade(grades)
    if avg is not None:
        print(f"The average grade for {course} is {avg:1f}.")
    else:
        print(f"The average grade for {course} could not be calculated due to missing data.")
