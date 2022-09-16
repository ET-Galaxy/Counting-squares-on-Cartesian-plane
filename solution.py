count=0
x=[-1,-1,-1,0,0,0,1]
y=[-1,0,1,-1,0,1,0]
ptlist=[[x[i],y[i]] for i in range(0,len(x))]  #list of points using coordinates
def dist(a,b): #input 2 points here
    return (a[0]-b[0])**2+(a[1]-b[1])**2
linelist=[[i,j] for i in range(0,len(x)) for j in range(i,len(x)) if i!=j] #list of lines in terms of points
lenlist=[dist(ptlist[i], ptlist[j]) for i,j in linelist] #list of lengths
def slope(line):
    if x[line[0]]-x[line[1]]==0:
        return "NaN"
    else:
        return (y[line[0]]-y[line[1]])/(x[line[0]]-x[line[1]])
print(linelist)
slopelist=[slope(line) for line in linelist] #list of slopes
print(slopelist)
for i in set(lenlist):
    samelenindex=[j for j in range(len(lenlist)) if lenlist[j]==i]
    if len(samelenindex)>=4:
        possible=[[samelenindex[i],samelenindex[j],samelenindex[k],samelenindex[m]] for i in range(len(samelenindex)) for j in range(i+1, len(samelenindex)) for k in range(j+1, len(samelenindex)) for m in range(k+1, len(samelenindex))]
        for j in possible:
            squarepts=set(linelist[j[0]]+linelist[j[1]]+linelist[j[2]]+linelist[j[3]])
            if len(squarepts)==4:
                count+=1 #counting rhombuses
print(count)