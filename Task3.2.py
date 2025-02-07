#Task 3.2

fn = input("Enter First Name: ")
ln = input("Enter Last Name: ")

full_name = fn + " " +  ln
print("Full Name (Uppercase):", full_name.upper())
print("Full Name (Lowercase):", full_name.lower())

name_length = len(full_name.replace(" ", ""))
print("Length of your Full Name (excluding spaces):", name_length)