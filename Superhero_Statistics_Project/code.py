# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)
print(data.head())
print('---------------------------------------')

#Replacing - to agender and plotting gender graph
data['Gender']=data['Gender'].replace('-','Agender')

plt.figure(figsize=(12,7))
plt.xlabel('Gender')
plt.ylabel('Frequency')
gender=data['Gender'].value_counts()
plt.bar(gender.index,gender.values)
plt.show()

#Majority of heros are male

#alignment Distribution
plt.figure(figsize=(12,7))
plt.xlabel('Alignment')
plt.ylabel('Frequency')
align=data['Alignment'].value_counts()
plt.bar(align.index,align.values)
plt.show()

# Majority of heros are good
# No change in majority,  if the ones in neutral all took one side

#combat skills related to strength or intelligence
com_stn_coeff=data[['Combat','Strength']].corr(method='spearman')
print(com_stn_coeff)
print('-----------------------------------------------')
com_int_coeff=data[['Combat','Intelligence']].corr(method='spearman')
print(com_int_coeff)
print('-----------------------------------------------')

#Combat is related to both Intelligence and Strngth positively and linearly
# best of the best in this superhero universe

Quan99=data['Total'].quantile(0.99)
super_best_names=list(data['Name'][data['Total']>Quan99].values)
print(super_best_names)



# Code starts here



