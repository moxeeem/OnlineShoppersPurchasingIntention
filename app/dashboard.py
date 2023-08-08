from explainerdashboard import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV

RANDOM_STATE = 42
DATASET_PATH = 'https://raw.githubusercontent.com/aiedu-courses/stepik_eda_and_dev_tools/main/datasets/online_shoppers_intention.csv'

df = pd.read_csv(DATASET_PATH)

df.drop_duplicates(inplace=True)
df.reset_index(inplace=True, drop=True)

df['Informational_Duration'].fillna(df['Informational_Duration'].median(), inplace=True)
df['ProductRelated_Duration'].fillna(df['ProductRelated_Duration'].median(), inplace=True)
df = df.dropna(subset=['ExitRates'])
df['Month'] = df['Month'].replace('aug', 'Aug')

month_ordering = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df['Month'] = df['Month'].apply(lambda x: month_ordering.index(x))
dummies = pd.get_dummies(df['VisitorType'], prefix='VT', drop_first=True)
df = pd.concat([df, dummies], axis=1)
df = df.drop('VisitorType', axis=1)
df['Weekend'] = df['Weekend'].astype(int)
df['Revenue'] = df['Revenue'].astype(int)

X = df.drop('Revenue', axis=1)
y = df['Revenue']
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.3, random_state=RANDOM_STATE)

scaler = StandardScaler()
scaler.fit(Xtrain)

Xtrain = scaler.transform(Xtrain)
Xtest = scaler.transform(Xtest)

Xtrain = pd.DataFrame(Xtrain, columns=X.columns)
Xtest = pd.DataFrame(Xtest, columns=X.columns)

model = GaussianNB()

params = {'priors': [None, [0.7, 0.3], [0.3, 0.7], [0.8, 0.2], [0.2, 0.8], [0.9, 0.1], [0.1, 0.9]],
          'var_smoothing': [1e-9, 1e-8, 1e-7, 1e-6]}

gs = GridSearchCV(model, params, scoring='f1', cv=5, n_jobs=-1, verbose=2)

gs.fit(Xtrain, ytrain)

best_model = gs.best_estimator_

explainer = ClassifierExplainer(best_model, Xtest.iloc[:10], ytest.iloc[:10])
db = ExplainerDashboard(explainer)
db.to_yaml("dashboard.yaml", explainerfile="explainer.dill", dump_explainer=True)
