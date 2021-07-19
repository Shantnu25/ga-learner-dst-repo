# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
#Step1

bank=pd.read_csv(path)
# categorical_var for all categorical values
categorical_var=bank.select_dtypes(include='object')
print(categorical_var.shape)
print('------------------------------------------------')

# numerical_var for all numerical values
numerical_var=bank.select_dtypes(include='number')
print(numerical_var.shape)
print('------------------------------------------------')

#Step 2

banks=bank.drop(['Loan_ID'],axis=1)
print(banks.shape)
print('------------------------------------------------')

#To check null values
print(banks.isnull().sum())
print('------------------------------------------------')

#mode of df banks
bank_mode=banks.mode()
print(bank_mode)
print('------------------------------------------------')

#Filling missing(NaN) values with bank_mode
banks=banks.replace(np.nan,bank_mode)
print(banks.isnull().sum().values.sum())
print('------------------------------------------------')

#Step 3

#check the loan amount of an average person using pivot table

avg_loan_amount=pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount')
print(avg_loan_amount)
print('------------------------------------------------')

#Step 4

#check the percentage of loan approved based on a person's employment type
loan_approved_se=len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')])
print(loan_approved_se)

loan_approved_nse=len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])
print(loan_approved_nse)
Loan_Status=614
print('------------------------------------------------')

percentage_se=(loan_approved_se*100)/Loan_Status
print(percentage_se)

percentage_nse=(loan_approved_nse*100)/Loan_Status
print(percentage_nse)
print('------------------------------------------------')

#Step 5

loan_term=banks['Loan_Amount_Term'].apply(lambda x:(x/12))

big_loan_term=len(loan_term[loan_term >=25])
print(big_loan_term)
print('------------------------------------------------')

#Step 6
#check the average income of an applicant and the average loan given to a person based on their income
loan_groupby= banks.groupby('Loan_Status')

loan_groupby=loan_groupby['ApplicantIncome', 'Credit_History']
mean_values=loan_groupby.mean()
print(mean_values.iloc[1,0], 2)
print('------------------------------------------------')



