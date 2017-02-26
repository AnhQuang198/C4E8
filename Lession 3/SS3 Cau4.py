ship_size = [5, 15, 20, 115, 200, 50]
print("Hello, my name is Quang and these are my ship sizes")
print(ship_size)
print ("Now my biggest sheep has size", max(ship_size) ,"let's shear it")
print("After shearing, here is my flock")
ship_size.remove(max(ship_size))
print(ship_size)
for j in range(1,len(ship_size)):
    print("MONTH",j)
    for i in range(len(ship_size)):
        ship_size[i]=ship_size[i]+50
    ship_size.index(max(ship_size))
    ship_size[ship_size.index(max(ship_size))]=8
    print("One month has passed, now here is my flock")
    print(ship_size)
    print("After shearing, here is my flock")
sum(ship_size)
print("My flock has size in total: ",sum(ship_size))
a=sum(ship_size)*2
print("I would get",a,"$")
        

