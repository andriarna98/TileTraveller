# 9 if statements sem kanna hvar leikmadur er staddur a x/y
# True/False fyrir directions sem eru i bodi
# Ef direction er true tha er haegt ad fara i tha att
# alltaf kannad fyrst ef x er 3 og y er 1, ef thad er satt tha kemur victory
x = 1
y = 1
Max_number = 3

while (True):
    if (x == 1 and y == 1) or (x == 2 and y == 1):
        print("You can travel: (N)orth.")
    elif x == 1 and y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif x == 1 and y == 3:
        print("You can travel: (E)ast or (S)outh.")
    elif (x == 2 and y == 2) or (x == 3 and y == 3):
        print("You can travel: (S)outh or (W)est.")
    elif x == 2 and y == 3:
        print("You can travel: (E)ast or (W)est.")   
    elif x == 3 and y == 2:
        print("You can travel: (N)orth or (S)outh.")
    elif x == 3 and y == 1:
        print("Victory!")
        break
    while x<=Max_number and y<=Max_number:
        d = input("Direction: ")
        if d == "n" or d == "N":
            if y == Max_number or (x==2 and y ==2):
                print("Not a valid direction!")
            else:
                y += 1
                break

        elif d == "w" or d == "W":
            if x == 1 or (x==2 and y==1) or (x==3 and y==2) or (x==3 and y==1):
                print("Not a valid direction!")
            else:
                x -=1
                break

        elif d == "e" or d == "E":
            if x == Max_number or (x==2 and y==2) or (x==2 and y==1) or (x==1 and y==1):
                print("Not a valid direction!")
            else:
                x +=1
                break
        elif d == "s" or d == "S":
            if y == 1 or (x==2 and y==3):
                print("Not a valid direction!")
            else:
                y -=1
                break