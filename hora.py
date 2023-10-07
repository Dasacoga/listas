def tiempoo(matriz,minutosfinal):
    conteo=-1
    for i in matriz:
        i=str(i)
        conteo=conteo+1
        min=0
        hor=0
        seg=0

        for k in i:
            if (k=="m"):
                min=1
        for k in i:
            if (k=="h"):
                hor=1
        for k in i:
            if (k=="s"):
                seg=1

        if (min==1 and hor==0):
            minutosfinal[conteo]=int(i[0]+i[1])
            
        elif (min==0 and hor==1):
            horasfinal=int(i[0])
            minutosfinal[conteo]=horasfinal*60

        elif (min==1 and hor==1):
            horasfinal=int(i[0])
            minutos=int(i[4]+i[5])
            minutosfinal[conteo]=horasfinal*60+minutos

        elif (seg==1):
            minutosfinal[conteo]=0
        
    

