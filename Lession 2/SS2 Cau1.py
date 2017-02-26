##1. Boolean la mot gia tri True hoac False
##+ x = 4
##  x == 4
##+ 10==(7+3)
##+ x = "Q"
##  x + "uang" == "Quang"

##3
##nested conditionals (dk long nhau): la trong dieu kien lai co mot dieu kien khac

x=int(input("Nhap x="))
if x < 0:
    print("x la so am")
else:
    if x >= 5:
        print(x)
    else:
        print("x la so duong nho hon 5 ^^!")

