#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)
print(data.head())
print('---------------------------------------')

#1 Checking the distribution of Gender (Male, Female, Agender)

#Replacing '-' to 'agender' and plotting gender graph
data['Gender']=data['Gender'].replace('-','Agender')

#Storing the value counts of 'Gender'
gender_count=data['Gender'].value_counts()

#Plotting bar graph of 'gender_count'
plt.figure(figsize=(12,7))
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.bar(gender_count.index,gender_count.values)
plt.show()

#Obs: Majority of heros are male

#2 Character Alignment Distribution (Good, Bad, Neutral)

#Storing the value count of 'Alignment' 
align=data['Alignment'].value_counts()

#Plotting bar chart for 'alignment'
plt.figure(figsize=(12,7))
plt.xlabel('Alignment')
plt.ylabel('Frequency')
plt.title('Character alignment')
plt.bar(align.index,align.values)
plt.show()

# Majority of heros are good
# No change in majority,  if the ones in neutral all took one side

#3 Checking combat skills related to strength or intelligence (correlation)

#Combat - strength corr
com_stn_coeff=data[['Combat','Strength']].corr(method='spearman')
print(com_stn_coeff)

#Combat - intelligence corr
com_int_coeff = data[['Combat','Intelligence']].corr(method='spearman')
print(com_int_coeff)

#Combat is strongly positively correlated to both Intelligence(0.75) and Strngth(0.74)

#4 Finding names of best of the best in this superhero universe

#by finding q = 0.99 for Total column
Quan99 = data['Total'].quantile(0.99)

#List of superhero names in 0.99 quantile
super_best_names = list(data['Name'][data['Total']>Quan99].values)
print(super_best_names)



# Code starts here
