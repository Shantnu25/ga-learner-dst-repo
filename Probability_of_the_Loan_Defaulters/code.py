# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)
print(df.head(2))

tot=len(df)
print(tot)
print('------------------------------------')

#Task 1: To calculate the joint probability
p_a=len(df[df['fico']>700])/tot
print(p_a)
print('------------------------------------')

p_b=len(df[df['purpose']== 'debt_consolidation'])/tot
print(p_b)

df1=df[df['purpose']== 'debt_consolidation']

p_a_b=((len(df1[df1['fico']>700]))/tot)/p_b
print(p_a_b)

result=p_a_b==p_a
print(result)
print('------------------------------------')

#Task 2. Calculating conditional probability
prob_lp=len(df[df['paid.back.loan']=='Yes'])/tot
print(prob_lp)
print('------------------------------------')

prob_cs=len(df[df['credit.policy']=='Yes'])/tot
print(prob_cs)
print('------------------------------------')

new_df=df[df['paid.back.loan']== 'Yes']

prob_pd_cs=((len(new_df[new_df['credit.policy']=='Yes']))/tot)/prob_lp
print(prob_pd_cs)
print('------------------------------------')

bayes=(prob_pd_cs*prob_lp)/prob_cs
print(bayes)

#Task 3. Let's visualize the bar plot for the purpose
purp=df['purpose'].value_counts()

plt.figure(figsize=[12,7])
plt.xlabel('Purpose')
plt.ylabel('Frequency')
plt.bar(purp.index,purp.values)
plt.show()

df1=df[df['paid.back.loan']=='No']
print(df1.shape)

purp1=df1['purpose'].value_counts()
plt.figure(figsize=[12,7])
plt.xlabel('Purpose where paid.back.loan is No ')
plt.ylabel('Frequency')
plt.bar(purp1.index,purp1.values)
plt.show()

#Task 4. Let's plot the histogram for visualization of the continuous variable

inst_median=df['installment'].median()
print(inst_median)
inst_mean=df['installment'].mean()
print(inst_mean)

plt.figure(figsize=[12,7])
plt.xlabel(' installment')
plt.ylabel('Frequency')
plt.hist(df['installment'],bins=25)
plt.show()

plt.figure(figsize=[12,7])
plt.xlabel('log annual income')
plt.ylabel('Frequency')
plt.hist(df['log.annual.inc'],bins=25)
plt.show()


#Code starts here




