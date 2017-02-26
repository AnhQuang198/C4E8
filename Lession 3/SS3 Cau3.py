clothes = ["T-Shirt", "Sweater" ]
while True:
    a=input("welcome to our shop, what do you want (C, R, U, D)?")
    b=a.lower()
    if ( b == "c" ):
        new_clothes = input("Enter new item: ")
        clothes.append(new_clothes)
        print(clothes)
    elif ( b == "r" ):
        for i in range(len(clothes)):
            print(clothes[i], end =" ")
    elif ( b == "u" ):
        position = int(input("Update position: "))
        new_item = input("New item: ")
        clothes[position - 1] = new_item
        print("Our items:", end="")
        for i in range(len(clothes)-1):
            print(clothes[i], end=" ")
            print(clothes[len(clothes)-1])
        
