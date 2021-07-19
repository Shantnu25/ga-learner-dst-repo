# --------------
# Importing packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')

#Reading file
bank = pd.read_csv(path)

#1 - checking which variable is categorical and which one is numerical

# categorical_var for all categorical values
categorical_var = bank.select_dtypes(include='object')
print(categorical_var.shape)
print('------------------------------------------------')

# numerical_var for all numerical values
numerical_var=bank.select_dtypes(include='number')
print(numerical_var.shape)
print('------------------------------------------------')

#2  Sometimes customers forget to fill in all the details or they don't want to share other details.
#   Because of that, some of the fields in the dataset will have missing values.

# checking which columns have missing values and also the count of missing values each column has. 

# drop the Loan_ID
banks=bank.drop(['Loan_ID'],axis=1)
print(banks.shape)
print('------------------------------------------------')

# checking  all the missing values filled.
print(banks.isnull().sum())
print('------------------------------------------------')

#mode of df banks
bank_mode=banks.mode()
print(bank_mode)
print('------------------------------------------------')

#Filling missing(NaN) values with bank_mode
banks=banks.replace(np.nan,bank_mode)

# check again all the missing values filled.
print(banks.isnull().sum().values.sum())
print('------------------------------------------------')

#3 checking the loan amount of an average person based on 'Gender', 'Married', 'Self_Employed'.
# This will give a basic idea of the average loan amount of a person.

#check the loan amount of an average person using pivot table
avg_loan_amount=pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount')
print(avg_loan_amount)
print('------------------------------------------------')

#4 checking the percentage of loan approved based on a person's employment type.

# loan aprroved for self employed
loan_approved_se=len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')])
print(loan_approved_se)

#loan approved for non self employed
loan_approved_nse=len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])
print(loan_approved_nse)

Loan_Status=614
print('------------------------------------------------')

# percentage of loan approved for self employed
percentage_se=(loan_approved_se*100)/Loan_Status
print(percentage_se)

#percentage of loan for non self employed
percentage_nse=(loan_approved_nse*100)/Loan_Status
print(percentage_nse)
print('------------------------------------------------')

#5 company wants to find out those applicants with long loan amount term. 

loan_term=banks['Loan_Amount_Term'].apply(lambda x:(x/12))

big_loan_term=len(loan_term[loan_term >=25])

print(big_loan_term)
print('------------------------------------------------')

#6  checking the average income of an applicant and the average loan given to a person based on their income.

columns_to_show = ['ApplicantIncome', 'Credit_History']
 
loan_groupby=banks.groupby(['Loan_Status'])

loan_groupby=loan_groupby[columns_to_show]

# Check the mean value 
mean_values=loan_groupby.agg([np.mean])
print(mean_values)


