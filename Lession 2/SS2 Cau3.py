x=float(input("Nhap chieu cao: "))
y=float(input("Nhap can nang: "))
a = x/100      #doi tu cm sang m
BMI= y / (a*a)
if BMI < 16:
    print("Severely underweight")
elif BMI > 16 and BMI < 18.5:
    print("Underweight")
elif BMI > 18.5 and BMI < 25:
    print("Normal")
elif BMI > 25 and BMI < 30:
    print("Overweight")
else:
    print("Obese")
    
