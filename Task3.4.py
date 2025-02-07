#Task 3.4

print("Enter your Personal Details below:")
ln = input ("Enter last name: ")
fn = input ("Enter first name: ")
age = input ("Enter age: ")
contact_num = input ("Enter Contact Number: ")
course = input ("Enter your course: ")
student_info = f"Last Name: {ln}\n First Name: {fn}\n Age: {age}\n Contact Number: {contact_num}\n Course: {course}\n\n"
with open("student.txt", "a")as file:
    file.write(student_info)
print("Your Student Information has been saved sucessfully")

try:
    with open("student.txt", "r") as file:
        student_data = file.read()
    if student_data:
        print("Student Information: ")
        print(student_data)
    else:
        print("No data found.")
except FileNotFoundError:
    print("The file 'students.txt does not exist. Please add student information first.")   