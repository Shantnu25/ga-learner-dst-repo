# --------------
import pandas as pd 
import matplotlib as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

#1 Combine two excel sheets a single dataframe

offers=pd.read_excel(path, sheet_name=0)
transactions=pd.read_excel(path, sheet_name=1)

#print(offers.head())
#print(transactions.head())

#Adding new column 'n' to transactions
transactions['n']=1

#merging both offers and transactions to df
df = pd.merge(offers, transactions, on="Offer #")
print(df.shape)

#2 Creating an Offer-Transaction pivot table

#grouping df data by Offer # for every customer
matrix=df.pivot_table(index='Customer Last Name', columns='Offer #',values='n')

#lot of missing values (since every customer did not purchase all the offers)
#Fill in the missing values by 0s.
matrix.fillna(0, inplace=True)

# last names of customers are on the index; translating it to a column
matrix.reset_index(inplace=True)

print(matrix.shape)
#print(matrix.head())

#3 Using Kmeans to cluster data

clf= KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10,random_state=0)

# To store the cluster centers for every observation from matrix
matrix['cluster'] = clf.fit_predict(matrix[matrix.columns[1:]])

#print(matrix.head())
print(matrix.shape)

#4 Visualize clusters using PCA
 
# Data at hand is multidimensional, you cannot simply do it on a 2-D graph.
# Using PCA to reduce the dimensionality to two dimensions to visualize the clusters

pca =  PCA(n_components=2, random_state=0) 

# X co-ordinates of every observation in decomposed form
matrix['x'] = pca.fit_transform(matrix[matrix.columns[1:]])[:,0]

# Y co-ordinates of every observation in decomposed form
matrix['y'] = pca.fit_transform(matrix[matrix.columns[1:]])[:,1]

#Cluster containing column number of columns - 
#customer names, cluster it belongs to and X and Y co-ordinates of every observation respectively. 
clusters= matrix.iloc[:,[0, 33, 34, 35]]

# visualzie data points according to clusters
matrix.plot.scatter(x='x', y='y', c='cluster', colormap='viridis')

print(matrix.shape)

#5 Which cluster orders the most Champagne?

#merge dataframes clusters and transactions
data = clusters.merge(transactions)

# merge offers and data
data = data.merge(offers)

#Initialize an empty dictionary champagne
champagne={}

#Iterate over every cluster
for i in range(0,5):
    # observation falls in that cluster
    new_df = data[data['cluster'] == i]
    # sort cluster according to type of 'Varietal'
    counts=new_df['Varietal'].value_counts(ascending=False)
    # check if 'Champagne' is ordered mostly
    if counts.index[0] == 'Champagne':
        # add it to 'champagne'
        champagne.update({i:counts[0]})

# get cluster with maximum orders of 'Champagne' 
cluster_champagne = max(champagne, key=champagne.get)

# print out cluster number
print(cluster_champagne)

#6 Which cluster of customers favours discounts more on an average?

#Initialize empty dic - discount 
discount={}

# iterate over cluster numbers
for i in range(0,5):
    # dataframe for every cluster
    new_df = data[data['cluster'] == i]
    # average discount for every cluster
    counts = new_df['Discount (%)'].values.sum() / len(new_df)
    # adding cluster number as key and average discount as value
    discount.update({i:counts}) 

print(discount)

# cluster with maximum average discount
cluster_discount = max(discount, key = discount.get)
print(cluster_discount)






