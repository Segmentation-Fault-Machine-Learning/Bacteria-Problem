#visalizando um dado muiltidimensional com o T-SNE
import sklearn.manifold as sk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../processamento_de_dados/result.csv')
sv = np.asarray(data['Tipo'])
#retirnado dado do DataFrame


del (data['Tipo'])


tsne = sk.TSNE(n_components=2, random_state=0)

teste1 = tsne.fit_transform(data)

color={3:'red', 1:'yellow', 2:'green'}
marcadores={3:'s',2:'d',1:'p'}
plt.figure()

plt.title("Visualização dos dados por T-SNE")

for cl in range(0,150):
		cor = color[sv[cl]]
		mark = marcadores[sv[cl]]
		plt.scatter(teste1[cl,0],teste1[cl,1],c=cor,marker=mark,s=40)

plt.xlim([-350,350])
plt.ylim([-350,350])
plt.legend(['Bacteria 1', 'Bacteria 2','Bacteria 3'],loc='upper left')
plt.show()
