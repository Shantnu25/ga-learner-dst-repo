#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')

#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Reading file
data=pd.read_csv(path)

#Code starts here

#1 Finding the Confidence Interval

#Sampling the dataframe
data_sample=data.sample(n=sample_size,random_state=0)

#Finding the mean of the sample
sample_mean=data_sample['installment'].mean()

#Finding the standard deviation of the sample
population_std = data['installment'].std()

#Finding the margin of error
margin_error=(z_critical*population_std)/math.sqrt(sample_size)

#Finding the confidence interval
confidence_interval= (sample_mean-margin_error,sample_mean+margin_error)
print('Confidence interval:', confidence_interval)

#Finding the true mean
true_mean=data['installment'].mean()
print('True mean:', true_mean)
print('--------------------------------------')

#2 Chiecking if CLT holds for installment column

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Creating different subplots
fig,axes=plt.subplots(3,1, figsize=(10,20))

#Running loop to iterate through rows
for i in range(len(sample_size)):
    
    #Initialising a list
    m=[]
    
    #Loop to implement the no. of samples
    for j in range(1000):
        
        #Finding mean of a random sample
        mean=data['installment'].sample(sample_size[i]).mean()
        
        #Appending the mean to the list
        m.append(mean)
        
        
    #Converting the list to series
    mean_series=pd.Series(m)   

    #Plotting the histogram for the series
    axes[i].hist(mean_series, normed=True)

#Displaying the plot
plt.show()

#3 Small Business Interests
# The bank manager believes that people with purpose as 'small_business' 
# have been given int.rate more due to the risk assosciated.
# Hypothesis testing(one-sided)

#Null Hypothesis H0: μ= 12 % i.e There is no difference in interest rate being given to people with purpose as 'small_business' 

#Alternate Hypothesis H1: μ>12 % i.e.Interest rate being given to people with purpose as 'small_business' is higher than the average interest rate

# Removing the last character from the values in column
data['int.rate'] = data['int.rate'].map(lambda x: str(x)[:-1])

#Dividing the column values by 100
data['int.rate']=data['int.rate'].astype(float)/100

#Applying ztest for the hypothesis
z_statistic_1, p_value_1 = ztest(x1=data[data['purpose']=='small_business']['int.rate'], value=data['int.rate'].mean(), alternative='larger')

print(('Z-statistic 1 is :{}'.format(z_statistic_1)))
print(('P-value 1 is :{}'.format(p_value_1)))

#4 Installment vs Loan Defaulting
# The bank thinks that monthly installments (installment column) 
# customers have to pay might have some sort of effect on loan defaulters.

#Null Hypothesis: There is no difference in installments being paid by loan defaulters and loan non defaulters

#Alternate Hypothesis: There is difference in installments being paid by loan defaulters and loan non defaulters

#Applying ztest for the hypothesis
z_statistic_2, p_value_2 = ztest(x1=data[data['paid.back.loan']=='No']['installment'], x2=data[data['paid.back.loan']=='Yes']['installment'])

print(('Z-statistic 2 is :{}'.format(z_statistic_2)))
print(('P-value 2 is :{}'.format(p_value_2)))


#5 Purpose vs Loan Defaulting (both categorical columns)
#Another thing bank suspects is that there is a strong association between purpose of the loan(purpose column) of a person and whether that person has paid back loan (paid.back.loan column)

#Null Hypothesis : Distribution of purpose across all customers is same.

#Alternative Hypothesis : Distribution of purpose for loan defaulters and non defaulters is different.

# Subsetting the dataframe
yes=data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
no=data[data['paid.back.loan']=='No']['purpose'].value_counts()

#Concating yes and no into a single dataframe
observed=pd.concat([yes.transpose(),no.transpose()], 1,keys=['Yes','No'])
print(observed)

chi2, p, dof, ex = chi2_contingency(observed)

if chi2 > critical_value:
    print('Rejct the null Hypothesis')
else:
    print('Null Hypothesis can not be rejected')
