import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from random import randint
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.inspection import DecisionBoundaryDisplay

'''
+=============================================+
+PESO            SUPERFICIE      RESULTADO    +
+=============================================+
+LARANJA         IRREGULAR       130-142      +
+TANGERINA       IRREGULAR       112-120      +
+LIMAO           IRREGULAR       92-100       +
+MORANGO         IRREGULAR       08-14        +
+=============================================+
+PESO            SUPERFICIE      RESULTADO    +
+=============================================+
+MAÇA            LISA            132-140      +
+PERA            LISA            118-126      +
+BANANA          LISA            78-86        +
+UVA             LISA            04-10        +
+=============================================+
'''
rosa = '\033[1;26;41m]'

# Define the classes and features
CLASSES = {
    'LARANJA': 0,
    'MAÇÃ': 1,
    'MORANGO': 2,
    'BANANA': 3,
    'PERA': 4,
    'TANGERINA' : 5,
    'UVA' : 6,
    'LIMÃO': 7,
    'DADOS INVALIDOS': 8
}

FEATURES = {'lisa': 1, 'irregular': 0, 'peso': 0, 'superficie': 1, 'invalido': 0.5}

# Define the training and test data
TRAIN_DATA = [    
    [140, FEATURES['lisa'], CLASSES['MAÇÃ']],
    [132, FEATURES['lisa'], CLASSES['MAÇÃ']],
    [142, FEATURES['irregular'], CLASSES['LARANJA']],
    [130, FEATURES['irregular'], CLASSES['LARANJA']],
    [14, FEATURES['irregular'], CLASSES['MORANGO']],
    [8, FEATURES['irregular'], CLASSES['MORANGO']],
    [86, FEATURES['lisa'], CLASSES['BANANA']],
    [78, FEATURES['lisa'], CLASSES['BANANA']],
    [126, FEATURES['lisa'], CLASSES['PERA']],
    [118, FEATURES['lisa'], CLASSES['PERA']],
    [120, FEATURES['irregular'], CLASSES['TANGERINA']],
    [112, FEATURES['irregular'], CLASSES['TANGERINA']],
    [10, FEATURES['lisa'], CLASSES['UVA']],
    [4, FEATURES['lisa'], CLASSES['UVA']],
    [100, FEATURES['irregular'], CLASSES['LIMÃO']],
    [92, FEATURES['irregular'], CLASSES['LIMÃO']],
    [65, FEATURES['invalido'], CLASSES['DADOS INVALIDOS']],
    [20, FEATURES['invalido'], CLASSES['DADOS INVALIDOS']]
]

p = []
for i in range(100):
    n = randint(0, 165)
    p.append(n)


m = []
for i in range(100):
    n = randint(0, 1)
    m.append(n)

for i in range(len(p)):
    if 16 <= p[i] <= 70:
        m[i] = 0.5

TEST_DATA = []
n = 100
for i in range(n):
    TEST_DATA.append([p[i], m[i]])


# Train a decision tree classifier
X_train = [[row[FEATURES['peso']], row[FEATURES['superficie']]] for row in TRAIN_DATA]
y_train = [row[-1] for row in TRAIN_DATA]

clf = tree.DecisionTreeClassifier(max_depth=9, max_leaf_nodes = 9)
clf.fit(X_train, y_train)

for i in range(len(m)):
    if m[i] == 1:
        m[i] = 'Lisa'
    else:
        m[i] = 'Irregular'       

print('==' * 30)
# Test the classifier with the test data
# Test the classifier with the test data
print('Results:')
print('..' * 30)
result_dict = {}
for i, data in enumerate(TEST_DATA):
    peso, superficie = data
    resultado = clf.predict([[peso, superficie]])
    for classe, valor in CLASSES.items():
        if valor == resultado[0]:
            print(f'Test {i+1}: {classe} ==> {peso}g > {m[i]}')
            if classe not in result_dict:
                result_dict[classe] = 0
            result_dict[classe] += 1
            break

print('==' * 30)
# Show the number of times each fruit was classified
print('Unidade de frutas:')
print('..' * 30)
for classe, quantidade in result_dict.items():
    print(f'{classe}: {quantidade}')
print('==' * 30)

# Plot the decision boundary and the test results
plt.figure(figsize=(6,4))
for fruta, valor in CLASSES.items():
    color = plt.cm.tab10(valor / len(CLASSES))
    mask = [y_train == valor for valor in CLASSES.values()]
    plt.scatter([row[FEATURES['peso']] for row in TRAIN_DATA if row[-1] == valor], 
                [row[FEATURES['superficie']] for row in TRAIN_DATA if row[-1] == valor],
                color=color, s=100, alpha=0.5, label=fruta)


plt.xlabel('Peso (g)')
plt.ylabel('Superficie (lisa=1, irregular=0)')
plt.title('Árvore de Decisão para Frutas')
plt.legend()


for i, data in enumerate(TEST_DATA):
    peso, superficie = data
    resultado = clf.predict([[peso, superficie]])
    color = plt.cm.tab10(resultado[0] / len(CLASSES))
    plt.scatter(peso, superficie, color=color, edgecolor='black', s=30, alpha=0.9)
    

# Count the predictions for each fruit
predictions = clf.predict(X_train)
fruit_counts = {classe: 0 for classe in CLASSES}
for prediction in predictions:
    for classe, valor in CLASSES.items():
        if valor == prediction:
            fruit_counts[classe] += 1
            break

# Calculate the accuracy of the classifier on the training data
y_pred_train = clf.predict(X_train)
acc_train = accuracy_score(y_train, y_pred_train)
print(f"Acurácia no conjunto de treinamento: {acc_train:.2%}")

iris = load_iris()

plt.figure()
clf = DecisionTreeClassifier().fit(iris.data, iris.target)
plot_tree(clf, filled=True)
plt.title("Decision tree trained on all the iris features")

plt.legend(fontsize = 8)
plt.show()
 



