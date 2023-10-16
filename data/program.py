v = open('data/02459.txt','w')
r = v.read()
v.close()
y = r.split('%')
d =  open('data/02459.txt','r')
for p in y:
        u = p.split('-')
        d.write(u[0])
        d.write(' ')
        d.write(u[1])
        d.write('\n')

d.close()
v = open('data/02459.txt','r')
k = v.read()
print(k)
v.close