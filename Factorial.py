from math import prod


userinput = input("Enter a whole number to find its factorial: ")
userstuff = int(userinput)
liststuff = []
while userstuff > 1:
    liststuff.append(userstuff)
    userstuff = userstuff - 1

print(prod(liststuff))