# Determinando os parametros a ser testados
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, balanced_accuracy_score
from sklearn.model_selection import train_test_split

X = [[1, 2, 3, 4],  
     [4, 5, 6, 7],  
     [7, 8, 9, 8],
     [1, 5, 7, 9]]
y = [0, 1, 1, 0] 
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, random_state=0)
meu_pipeline = Pipeline(steps=[
  ("normalizacao", MaxAbsScaler()),  
  ("MLP", MLPClassifier())
])
meu_pipeline.fit(X_treino, y_treino)
y_pred = meu_pipeline.predict(X_teste)
print(f"Acuracia: {accuracy_score(y_teste, y_pred)}")
print(f"Acurácia balanceada: {balanced_accuracy_score(y_teste, y_pred)}")
from sklearn.model_selection import GridSearchCV
param_busca={
  'MLP__learning_rate_init': [0.1, 0.01, 0.001]
}
buscador = GridSearchCV(estimator=meu_pipeline, param_grid=param_busca, cv=2)
buscador.fit(X, y)# realizando a busca
print("Melhor LR:", buscador.best_params_)
print("Score:", buscador.score)