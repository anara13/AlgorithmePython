def mystere(x,y):
    x=str
    y=int

    i,j,p=int
    z,t=str
    j=long(x)
    z=""

    for i in range(0,j-1):
        p=codeASCII(extrait(x,i,1))-65
        p=((p+y)mod 26)+65
        t=carASCII(p)
        z=z+t
    i++
    return z




