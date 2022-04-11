
def fonction():
    Note_obligatoire=[0,0,0,0,0,0,0]
    Note_obligatoire[0]=int(input("Saisir Note Fançais"))
    Note_obligatoire[1]=int(input("Saisir Note Maths"))
    Note_obligatoire[2]=int(input("Saisir Note Histoire géographie"))
    Note_obligatoire[3]=int(input("Saisir Note LV1"))
    Note_obligatoire[4]=int(input("Saisir Note LV2"))
    Note_obligatoire[5]=int(input("Saisir Note Physique"))
    Note_obligatoire[6]=int(input("Saisir Note Technologie"))
    note_option=int(input("Saisir Note Option, si pas d'option, saisir 0"))
    moyenne=0
    coefficients=[3,3,2,2,1,2,1]
    sommecoefs=14
    i=0
    sommepoints=0
    points_gagnes=0
    mention=("")

    for i in range (0,6):
        sommepoints=sommepoints+Note_obligatoire[i]*coefficients[i]
        i=i+1

    if (note_option<10):
        points_gagnes=0

    else:
        points_gagnes=note_option-10
        points_gagnes=points_gagnes*2

    sommepoints=sommepoints+points_gagnes
    moyenne=sommepoints/sommecoefs

    if (moyenne<10):
        print ("Refusé à l'examen")

    elif(moyenne in range (10,12)):
        mention=(" Passable")

    elif(moyenne in range (12,14)):
        mention=(" Assez bien")

    elif(moyenne in range (14,16)):
        mention=("Bien")

    elif(moyenne in range (16,20)):
        mention=("Très bien")

    else:
        print("Recu à l'examen avec mention" +mention)










