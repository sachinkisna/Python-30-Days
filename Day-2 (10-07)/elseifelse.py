#Logical Operator 'and' 'or' 'not'
tenth=input("10th 'Pass' or 'fail'")
twelveth=input('12th "pass" or "fail"')
applied=True

if tenth=="pass" and twelveth=="pass":
    print("yor are eligabel")
elif tenth=="pass" or twelveth=="pass":
    print("Your are not eligable but by stand")

day=input("Enter the day")
if day in ("sunday","satarday"):
    print("Weekends")
else:
    print("Weekdays")

age=eval(input("Enter your age: "))
if 13 <= age <= 19:
    print("you are a teenger")
elif age<=13:
    print("Your are a kid")
else:
    print("Your are a Yong")

age=eval(input("Enter your age: "))
country=input("Enter your countray: ")

if age>=18:
    if country=="indian":
        print("You Can Vote")
    else:
        print("only for indian")
else:
    print("Your are not eligabele")