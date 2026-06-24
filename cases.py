import copy
print("\033[47;31m\n\ngive me the list file")
a=input().strip()
f1=open(a,"r")
b=f1.read()
f1.close()
c=b.split("|")
counter=0
g="""
match var0:
"""
h="""
    case \"$1\":
        var1=\"$2\"
"""
j=copy.copy(g)
print(j)
for z in range(0,len(c),2):
    k=copy.copy(h)
    k=k.replace("$1",c[z])
    k=k.replace("$2",c[z+1])
    print(k)