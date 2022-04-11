def image():

    tab=[[0,0,255,255],[255,255,255,255],[0,255,0,225],[0,0,255,0],[0,0,0,0]]
    TabRes=[]
    i=0
    j=0


    for i in range(0,4):
        for j in range(0,3):
            TabRes[i,j]=tab[4-i,j]

    return TabRes




