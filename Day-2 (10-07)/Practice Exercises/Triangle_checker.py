s1=eval(input('enter side1'))
s2=eval(input('enter side2'))
s3=eval(input('enter side3'))

if s1+s2>s3 and  s2+s3>s1 and s1+s3>s2:
    print("It Is a Tribnale")
else:
    print("not")