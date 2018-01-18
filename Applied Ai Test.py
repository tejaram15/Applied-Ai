import pandas as pd

print('Importing Data...')
train = pd.read_csv("train_data.csv",skiprows=1)
test = pd.read_csv("test_data.csv",skiprows=1)
print('Importing Complete...')

