import pandas as pd
import hora


doc=pd.read_excel("hoja.xlsx")

df=pd.DataFrame(doc)

horaminima=int(input("¿Cuales son los minutos minimos de asistencia? "))

m=-1
presente=[""]*len(df)
Col1=[""]*len(df)
Col2=[""]*len(df)
Col3=[""]*len(df)

for i in range(len(df)):
   m=m+1
   Col1[m]=df.iloc[i]['Correos misestu']
   Col2[m]=df.iloc[i]['Correos asistentes']
   Col3[m]=df.iloc[i]['Duracion']


m=-1
minutosfinal=[""]*len(Col3)
hora.tiempoo(Col3,minutosfinal)



for j in Col1:
   if j=="":
      break
   m=m+1
   presente[m]=0
   

   for k in range(len(df)):
      if str(j).lower()==str(Col2[k]).lower():
         if minutosfinal[k]>horaminima:
            presente[m]=1
         elif minutosfinal[k]<=horaminima:
            presente[m]=0

      
hoja_final=pd.DataFrame({"Correos misestu":Col1,"Presente":presente,"Correos asistentes":Col2,"Tiempo de asistencia":Col3,"Tiempo de asistencia minutos":minutosfinal})
hoja_final.to_excel('Resultado.xlsx', sheet_name='sheet1', index=False)