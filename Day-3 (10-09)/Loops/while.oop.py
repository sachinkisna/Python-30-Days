age=input("Enter Your Age")

while not age.isdigit():
    print("Enter DigitOnley")
    age = input("Enter Your Age")
age=int(age)
print(f"Your Age Is {age}")