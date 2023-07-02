# Dictionaries 
#   - Associate keys and values together
#   - Keys have to 'Strings' values and other hashable types 

friend_ages = {
    "Rolf": 24,
    "Jason": 34,
    "Cyrus": 1,
}

# Accessing one key and retrieving its value
print(friend_ages["Rolf"])

# Add a key-value to a dictionary
friend_ages["Bob"] = 20
print(friend_ages)

# Change a key-value of a dictionary
friend_ages["Bob"] = 33
print(friend_ages)

# Real world example - storing dictionaries inside lists 
#       - Easier access to wanted data
#       - Able to store more data in the dictionary for a specific index
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},    
]

print(friends) 
print(friends[2]["name"])
print("-----------")

# Iterate over dictionary
student_attendance = {
    "Rolf": 96,
    "Bob": 80,
    "Anne": 100,
}

#   - Print the keys in the dictionary using For-Loop
for student in student_attendance:
    print(student)
    # to get the value
    print(f"{student}: {student_attendance[student]}")
    
# Better ways of Iterating over Dictionaries
#   - printing both key and value
for student, attendance in student_attendance.items():
    print(f"{student} - {attendance}")    
    
# Check if a key is in the dictionary
if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student in this class")
    
# Getting only the values of the keys in the dictionary    
attendance_values = student_attendance.values()
print(attendance_values)
print(len(attendance_values))
print(sum(attendance_values) / len(attendance_values)) #calculate the averages 