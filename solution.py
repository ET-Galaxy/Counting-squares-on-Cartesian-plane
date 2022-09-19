def countsquares(x,y):
    """
    returns the number of possible squares formed by given points on a Cartesian plane

    Args:
    x (arr): the x-coordinates of all given points
    y (arr): the y-coordinates of all given points 

    Returns:
    int
    """
    count=0
    ptlist=list(zip(x,y))  #list of points using coordinates
    def dist(a,b): #input 2 points here
        """
        returns distance between point a and point b

        Args:
        a (int): refers to point with index a given by ptlist
        b (int): refers to point with index b given by ptlist

        Returns:
        int
        """
        return (a[0]-b[0])**2+(a[1]-b[1])**2
    linelist=[[i,j] for i in range(0,len(x)) for j in range(i,len(x)) if i!=j] #list of lines in terms of points
    lenlist=[dist(ptlist[i], ptlist[j]) for i,j in linelist] #list of lengths
    def slope(line):
        """
        returns the slope of line

        Args:
        line (int): the line numbered according to linelist

        Returns:
        int
        """
        if x[line[0]]-x[line[1]]==0:
            return "NaN"
        else:
            return (y[line[0]]-y[line[1]])/(x[line[0]]-x[line[1]])
    def perpendicular(a,b):
        """
        returns whether 2 lines are perpendicular

        Args:
        a,b (1-by-2 array): the lines a,b, each described by 2 points [.,.]

        Returns:
        Boolean
        """
        if "NaN" in set([slope(a),slope(b)]):
            return 0 in set([slope(a),slope(b)])
        else:
            return slope(a)*slope(b)==-1

    for i in set(lenlist):
        samelenindex=[j for j in range(len(lenlist)) if lenlist[j]==i]
        if len(samelenindex)>=4:
            possible=[[samelenindex[i],samelenindex[j],samelenindex[k],samelenindex[m]] for i in range(len(samelenindex)) for j in range(i+1, len(samelenindex)) for k in range(j+1, len(samelenindex)) for m in range(k+1, len(samelenindex))]
            for j in possible:
                squarepts=list(set(linelist[j[0]]+linelist[j[1]]+linelist[j[2]]+linelist[j[3]]))
                if len(squarepts)==4:
                    if perpendicular(linelist[j[0]],linelist[j[1]]) or perpendicular(linelist[j[0]],linelist[j[2]]):
                        count+=1 
    return(count)

print(countsquares(x=[-1,-1,-1,0,0,0,1,1,1], y=[-1,0,1,-1,0,1,-1,0,1]))