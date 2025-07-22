import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import joblib

df = pd.read_csv('frutas.csv')

X = df[['Peso', 'Diametro']]
y = df['Tipo de fruta']

nova_fruta = [
    [170, 8.2]
]

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)


classe_prevista = knn.predict(nova_fruta)

nomes = ['Maçã', 'Laranja', 'Limão']
cores = ['red', 'orange', 'green']

joblib.dump(knn, 'modelo_classificacao_frutas.joblib')

# ----------------------------- Gráficos --------------------------------------------
plt.figure(figsize=(8,6))

for i in range(len(X)):
  plt.scatter(
      x=X.iloc[i, 0], # Pega os pesos
      y=X.iloc[i, 1], # Pega os diametros
      color= cores[y.iloc[i]],
      edgecolors='black',
      label=nomes[y[i]] if nomes[y[i]] not in plt.gca().get_legend_handles_labels()[1] else ""
              )

plt.scatter(
    x = nova_fruta[0][0],
    y = nova_fruta[0][1],
    color='blue',
    marker = 'X',
    s=100,
    label = 'Nova fruta'
)


plt.title('Classificação de Frutas')
plt.xlabel('Peso (g)')
plt.ylabel('Diâmetro (cm)')
plt.legend()
plt.grid(True)
plt.show()

print('-'*100)
print(f'A nova fruta é classificada como: {nomes[classe_prevista[0]]}')