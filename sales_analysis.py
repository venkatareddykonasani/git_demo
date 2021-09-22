import pandas as pd

data_path="https://raw.githubusercontent.com/venkatareddykonasani/Datasets/master/Superstore%20Sales%20Data/"
Sales=pd.read_csv(data_path+"Sales_by_country_v1.csv")
print(Sales.shape)
print(Sales.info())

print("unitsSold.mean is ", Sales["unitsSold"].mean())
print("salesChannels \n", Sales["salesChannel"].value_counts())

print("unitsSold.mean is ", Sales["unitsSold"].median())


#Describe
print(Sales["unitsSold"].describe())
print(Sales["custCountry"].value_counts())

#Describe
print(Sales["unitsSold"].describe())
print(Sales["custCountry"].value_counts())

#Describe
print(Sales["unitsSold"].describe())
print(Sales["custCountry"].value_counts())
