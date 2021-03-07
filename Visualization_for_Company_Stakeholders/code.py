#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#1 Visualizing the company's record with respect to loan approvals.

print(data.shape)

#Creating a new variable to store the value counts
loan_status=data['Loan_Status'].value_counts()

#Plotting bar plot
plt.bar(loan_status.index,loan_status.data)
plt.show()

#Company has more 'loan approvals'
print('----------------------------------------')

#2 Loan approval distribution across the regions.

#Plotting an unstacked bar plot
property_and_loan=data.groupby(['Property_Area','Loan_Status'])
property_and_loan=property_and_loan.size().unstack()
property_and_loan.plot(kind='bar',stacked=False,figsize=[15,10])

#Changing the x-axis label
plt.xlabel('Property Area')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)
plt.show()

#Semiurban region with the highest no. of loan approvals
#Rural region with lowest no. of loan approvals
#Semiurban region with the maximum difference between loan approvals and loan rejections
print('----------------------------------------')


#3 Does higher education result in a better guarantee in issuing loans? 

#Plotting a stacked bar plot
education_and_loan=data.groupby(['Education','Loan_Status'])
education_and_loan=education_and_loan.size().unstack()
education_and_loan.plot(kind='bar',stacked=True,figsize=[15,10])

#Changing the x-axis label
plt.xlabel('Education Status')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)
plt.show()

#- Graduate group has asked for higher loan services irrespective of the approval. 

print('----------------------------------------')

#4  Checking whether being graduate or not also leads to different loan amount distribution 

#Subsetting the dataframe based on 'Education' column
graduate=data[data['Education'] == 'Graduate']

#Subsetting the dataframe based on 'Education' column
not_graduate=data[data['Education'] == 'Not Graduate']

#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density',label='Graduate')

#Plotting density plot for 'Graduate'
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')

#For automatic legend display
plt.legend()

print('----------------------------------------')

#5 Cheecking correlation between the borrower's income and loan amount 

#Setting up the subplots
fig,(ax_1,ax_2,ax_3)=plt.subplots(nrows = 3 , ncols = 1,figsize=[20,10])

#Plotting scatter plot
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])

#Setting the subplot ax.legis title
ax_1.set_title('Applicant Income')

#Plotting scatter plot
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])

#Setting the subplot axis title
ax_2.set_title('Coapplicant Income')

#Creating a new column 'TotalIncome'
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']

#Plotting scatter plot
ax_3.scatter(data['TotalIncome'],data['LoanAmount'])

#Setting the subplot axis title
ax_3.set_title('Total Income')

# High Correlation between 'ApplicantIncome' and 'LoanAmount'
