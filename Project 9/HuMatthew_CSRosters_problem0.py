class_data_file = 'class_data.txt'
enrollment_data_file = 'enrollment_data.txt'

# Load class data into dictionary
class_data = {}
with open(class_data_file) as f:
    for line in sorted(f):
        course_id = line.strip().split(',')[0]
        class_data[course_id] = line.strip()






# Prompt user for course ID
course_id = input("Enter a course ID (i.e. CS0002, CS0004): ")

# Check if course ID is valid
while course_id not in class_data:
    print("Cannot find this course")

    course_id = input("Enter a course ID (i.e. CS0002, CS0004): ")



else:
    # Retrieve course title from class data
    course_title = class_data[course_id]
    print(f"The title of this class is: {course_title}")

    # Load enrollment data into list
    enrollment_data = []
    with open(enrollment_data_file) as f:
        for line in f:
            fields = line.strip().split(',')
            if fields[0] == course_id:
                enrollment_data.append(fields[1:])

    # Sort enrollment data by last name
    enrollment_data.sort(key=lambda x: x[0])

    # Print number of students enrolled in course
    num_students = len(enrollment_data)
    print(f"The course has {num_students} students enrolled")

    # Print names of students enrolled in course
    for student in enrollment_data:
        print(f"* {' '.join(student[::-1])}")
