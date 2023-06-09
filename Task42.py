import pandas as pd

data = pd.read_csv("california_housing_test.csv")
res = data[data['population'] == data['population'].min()].households.max()
print(res)
