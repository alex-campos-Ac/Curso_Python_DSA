import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import joblib

# 1. Carregar o dataset
df = pd.read_excel('elegibilidade_credito.xlsx')

# 2. Corrigir o score dividindo por 1e16
df['historico_pagamento (score)'] = df['historico_pagamento (score)'] / 1e16

# 3. Selecionar as variáveis (features) e o alvo (target)
X = df[['salario_anual', 'total_dividas', 'historico_pagamento (score)', 'idade', 'credito_solicitado']]
y = df['elegibilidade']

# 4. Normalizar os dados
scaler = StandardScaler()
X_normalizado = scaler.fit_transform(X)

# 5. Dividir entre treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_normalizado, y, test_size=0.2, random_state=42)

# 6. Treinar modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 7. Fazer uma previsão de exemplo
entrada = [[100000, 20000, 0.95, 35, 12000]]  # exemplo hipotético
entrada_normalizada = scaler.transform(entrada)
predicao = knn.predict(entrada_normalizada)

print('-' * 50)
print(f'Entrada: {entrada}')
print(f'Previsão da categoria: {predicao[0]}')

# 8. Salvar modelo e scaler
joblib.dump(knn, 'modelo_elegibilidade_credito.joblib')
joblib.dump(scaler, 'scaler_credito.joblib')
