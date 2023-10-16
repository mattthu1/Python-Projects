n = open('899542.txt','r')
z = n.read()
n.close()
c = z.split('-')

for u in c:
    m = u.find('@@@')
    print(u[:m],u[m+1:])
