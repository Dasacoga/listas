horas=["1 h 24 min","1 h","3 min"]

for i in horas:
    min=0
    hor=0

    for k in i:
        if (k=="m"):
            print("tiene minutos")
            min=1
        if (k=="h"):
            print("tiene horas")
            hor=1
    if min==1 & hor==0:
            minutototal=i[0]+i[1]
            print(minutototal)
    

