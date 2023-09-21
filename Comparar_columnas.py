import pandas as pd
Cadenaacomparar=["maria","juan","juana"]

doc=pd.read_excel("hoja.xlsx")

df=pd.DataFrame(doc)
print(df)
m=-1
presente=[""]*len(df)
Col1=[""]*len(df)
Col2=[""]*len(df)

for i in range(len(df)):
   m=m+1
   Col1[m]=df.iloc[i]['Correos misestu']
   Col2[m]=df.iloc[i]['Correos asistentes']

m=-1
for j in Col1:
   if j=="":
      break
   m=m+1
   presente[m]=0

   for k in Col2:
      if str(j).lower()==str(k).lower():
         presente[m]=1

      
hoja_final=pd.DataFrame({"Correos misestu":Col1,"Presente":presente,"Correos asistentes":Col2})
hoja_final.to_excel('Resultado.xlsx', sheet_name='sheet1', index=False)