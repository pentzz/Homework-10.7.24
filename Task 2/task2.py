grade:int = int(input("Please enter your grade: "))
if grade >-1 and grade <41:
  print("try harder next time...")
elif grade >40 and grade<61:
  print("you're getting there, need some more work")
elif grade>60 and grade<81:
  print("pretty good!")
elif grade>80 and grade<96:
  print("awesome!")
elif grade>95 and grade<101:
  print("excellent!!! You're a Star!")
else:
  print("illegal grade")