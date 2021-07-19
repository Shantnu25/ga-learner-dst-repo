# --------------
#Importing header files
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, LabelEncoder




#Loading the data
data=pd.read_csv(path)

#Code starts here
print(data.info())

#1 Checking Null Values
print(data.isnull().sum())

#Treating null values in Rating feature using mean value
meanValue=np.mean(data['Rating'])
data['Rating']=data['Rating'].fillna(meanValue)

#Treating null value other than Rating
data.dropna(inplace=True)
print(data.isnull().sum())

#2 Plotting Rating Histogram
sns.distplot(data['Rating'],kde = False)
plt.show()

#Subset of data for Rating>5
data=data[data['Rating']<=5]

#Plotting Rating(only <=5) Histogram
sns.distplot(data['Rating'],kde = False)
plt.show()

#3 Genres only one Genre per app
data['Genres'] = data['Genres'].str.split(';').str[0]

#print(data['Genres'].value_counts())

#4 Mean rating of every Genres(Highest and Lowest average rating)
print(data.groupby('Genres')[['Rating']].mean())


#5 Installs and Price column - convert to numeric
data['Installs'] = data['Installs'].str.split('+').str[0]
data['Installs'] = data['Installs'].str.replace(',', '')
data['Price'] = data['Price'].str.replace('$', '')

data['Installs'] = data['Installs'].astype(int)
data['Price'] = data['Price'].astype(float)

plt.scatter(data['Installs'], data['Rating']);
plt.show()

plt.scatter(data['Price'], data['Rating']);
plt.show()

#6 Last Updated column as datetype
data['Last Updated']=pd.to_datetime(data['Last Updated'], infer_datetime_format=True)

print(data.info())



