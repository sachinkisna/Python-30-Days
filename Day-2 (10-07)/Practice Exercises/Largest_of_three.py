num1=eval(input("Enter The Nuber-1: "))
num2=eval(input("Enter The Nuber-2: "))
num3=eval(input("Enter The Nuber-3: "))


if num1>num2 and num1>num3:
    print(f"{num1} is Greatest")
elif num2>num3 and num2>num3:
    print(f"{num3} is Greatest")
elif num1==num2 and num1==num3:
    print("All are same")
else:
    print(f"{num3} is greatest")