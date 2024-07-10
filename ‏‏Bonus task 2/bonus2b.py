slices:int= int(input("Please enter the number of slices: "))
friendsnum:int= int(input("Please enter the number of friends: "))

x:int=int(slices/friendsnum)
y:int=int(slices%friendsnum)

if (slices<1) :
    print("Please enter a vaild number of slices!")
elif (friendsnum<1):
    print("Please enter a vaild number of friends!")
elif (y==0):
    print(f"each of danny's friends got {x} slices, and there are no slices left!")
else:
    print(f"each of danny's friends got {x} slices, and {y} slices left!")