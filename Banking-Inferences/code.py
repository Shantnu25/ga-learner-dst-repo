# --------------
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

#Confidence Interval
data_sample=data.sample(n=sample_size,random_state=0)
print(data_sample.head())


sample_mean=data_sample['installment'].mean()
margin_error=(z_critical*data_sample['installment'].std())/math.sqrt(sample_size)

confidence_interval= (sample_mean-margin_error,sample_mean+margin_error)
print(confidence_interval)
print('--------------------------------------')

true_mean=data['installment'].mean()
print(true_mean)
print('--------------------------------------')

#CLT holds for installment column?

samp=np.array([20,50,100])
sample_means_20 = [data['installment'].sample(samp[0]).mean() for i in range(1000)]
sample_means_20=pd.Series(sample_means_20)
plt.figure(figsize=[14,7])
plt.hist(sample_means_20,bins=25)
plt.xlabel('Installment')
plt.ylabel('Frequency')

# Small Business Interests
x1=data['int.rate'][data['purpose']=='small_business']
x1=(x1.str.replace(r'\D', '').astype(int))/100
value=((data['int.rate'].str.replace(r'\D', '').astype(int))/100).mean()

# apply ztest 
z_statistic, p_value = ztest(x1,value=value,alternative='larger')


# print z statistic and p value
z_statistic_1=z_statistic
p_value_1=p_value
print(z_statistic_1)
print(p_value_1)



# Installment vs Loan Defaulting
x1=data['installment'][data['paid.back.loan']=='No']
x2=data['installment'][data['paid.back.loan']=='Yes']

stat, p_value = ztest(x1,x2,alternative='two-sided')
z_statistic_2=stat
p_value_2=p_value





# Purpose vs Loan Defaulting

yes=data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
no=data[data['paid.back.loan']=='No']['purpose'].value_counts()

observed=pd.concat([yes.transpose(),no.transpose()], 1,keys=['Yes','No'])

print(observed)

chi2, p, dof, ex = chi2_contingency(observed)

if chi2 > critical_value:
    print('Rejct the null Hypothesis')
else:
    print('Null Hypothesis can not be rejected')


