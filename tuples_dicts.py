# Part 2: Tuples and Dictionaries
# 1. Create a tuple containing the names of the twelve months
months = ("January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December")
# 2. Print the first and last month from the tuple
print(f"First month: {months[0]}")
print(f"Last month: {months[-1]}")
# 3. Attempt to modify the tuple to demonstrate immutability
try:
 months[0] = "NewMonth"
except TypeError as e:
 print(f"Tuples are immutable, error: {e}")
# 4. Create a dictionary with student names and grades
students = {
"Alice": 92,
"Bob": 85,
"Charlie": 78
}
# 5. Add a new student and grade, then print all names and grades
students["Diana"] = 95
print("\n--- Student Grades After Addition ---")
for name, grade in students.items():
 print(f"{name}: {grade}")
# 6. Update one of the existing student's grades, then print the updated entry
students["Bob"] = 89
print(f"\nUpdated Bob's grade: Bob: {students['Bob']}")
# 7. Print out each student's name and grade in a formatted way using a loop
print("\n--- Final Formatted Student Roster ---")
for name, grade in students.items():
 print(f"{name}: {grade}")
