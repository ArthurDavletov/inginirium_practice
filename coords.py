x, y = int(input()), int(input())
if y > 0:
    if x > 0:
        print("I")
    elif x < 0:
        print("II")
    else:
        print("On the y axis")
elif y < 0:
    if x < 0:
        print("III")
    elif x > 0:
        print("IV")
    else:
        print("On the y axis")
else:
    if x == 0:
        print("One the center")
    else:
        print("On the x axis")
