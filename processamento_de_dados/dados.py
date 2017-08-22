import pandas as pd	
import numpy as np

data = pd.read_csv('data_base.csv')

def replacing_point(data):
	for i in range(data.size):
		data[i] = data[i].replace(',','.')



#Solving dot problem
replacing_point(data['comprimento corpo'])
replacing_point(data['largura corpo'])
replacing_point(data['comprimento flagelo'])
replacing_point(data['largura flagelo'])

#problema de tipagem [ ficou feio]
data.to_csv('resultado.csv',index=False)
data = pd.read_csv('resultado.csv')


#add 2 new colums 
col1 = np.array(data['comprimento corpo'])
col2 = np.array(data['largura corpo'])

data['proporcao corpo'] = col1/col2

col1 = np.array(data['comprimento flagelo'])
col2 = np.array(data['largura flagelo'])


data['proporcao flagelo'] = col1/col2
#tratando coluna tipo

#split na palavra
for i in range(data['Tipo'].size):
	a,b = data['Tipo'][i].split()
	data['Tipo'][i] = b

#set de palavras
conjunto = set(data['Tipo'])

#mapeando 
mapa = dict()
for each in conjunto:
	print("O que é isso [%s] ?" %(each))
	mapa[each]=input()

#replacing
for i in range(data['Tipo'].size):
	data['Tipo'][i]=mapa[data['Tipo'][i]]


#verificação
print(data)

#salvando
data.to_csv('resultado.csv',index=False)
