x = 0
y = 0
z = 0
q = 0

for c in "Helllo World":
    if c.isupper():
        x +=1

    elif c.islower():
        y += 1

    elif c.isalpha():
        z += 1

    else:
        q +=1

print (x,y,z,q,sep="#",end="n")