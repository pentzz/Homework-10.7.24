slices:int= int(input("Please enter the number of slices: "))
x:int=int(slices/4)
y=slices%4

if slices<1 :
    print("Please enter a vaild number of slices!")
elif y==0:
    print(f"each of danny's friends got {x} slices, and there are no slices left!")
else:
    print(f"each of danny's friends got {x} slices, and {y} slices left!")