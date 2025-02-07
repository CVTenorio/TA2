#Task 3.1

fn = input("Enter First Name: ")
ln = input("Enter Last Name: ")

full_name = fn + " " + ln
sliced_name = fn[:3]
greeting_message = f"Hello {sliced_name}, Welcome to the program!"

print("\nFull Name:", full_name)
print("\nSliced Name:", sliced_name)
print(greeting_message)