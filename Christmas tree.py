
height = int(input("Put the height of the tree: "))

for i in range(1, (height * 2)):

        if (i %2 == 0):
            continue

        else:
            spaces_Amount = height - (i / 2)
            spaces = " " * int(spaces_Amount)
            star = "*" * i
            print(spaces + star)
