import pandas as pd 

#DataFrame a partir de diccionario de listas 
datos = {'no_control':['2259001','2259002','2259003','2259004'],
		'nombre':['Saul','Alan','Leal','Mauricio'],
		'edad':['24','22','30','25'],
		'semestre':['8','8','9','9'],	
}

df = pd.DataFrame(datos)
print(df)

#dataframe a partir de una lista de listas
df = pd.DataFrame([['Saul',8],['Alan',9],['Leal',8],['Mauricio',8]])
print(df)

#dataframe a partir de lista de diccionarios
df = pd.DataFrame([{'Nombre':'Saul','Edad':23},{'Nombre':'Alan','Edad':20},{'Nombre':'Leal','Edad':18},{'Nombre':'Mauricio','Edad':28}])
print(df)

#Crear un dataframe a partir de un csv 
df = pd.read_csv('alumnos.csv')

print(df)
print(df.info())
print(df.shape())
print(df.size)
print(df.head(3))
print(df.tail(3))

#Crear un dataframe a partir de un txt, delimitando por tabulacion 
df = pd.read_csv('alumnos_2.txt', sep='\t')
print(df)

print(df.iloc[3,1])
print(df.iloc[3])
print(df.loc[3, 'edad'])
print(df.loc[3, ('edad','semestre')])

df['estatus'] = pd.series(["Egresado", "Baja temporal", "Activo", "Titulado",])
df['promedio'] = pd.series([70,80,60,100,85,70,80,60,100,85])

print(df['promedio']/10)
