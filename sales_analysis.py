import pandas as pd

data_path="https://raw.githubusercontent.com/venkatareddykonasani/Datasets/master/Superstore%20Sales%20Data/"
Sales=pd.read_csv(data_path+"Sales_by_country_v1.csv")
print(Sales.shape)
print(Sales.info())
