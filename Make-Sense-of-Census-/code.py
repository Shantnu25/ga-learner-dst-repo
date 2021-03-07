# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file

#Loading data file and saving it into a new numpy array 
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data.shape)

#add a new record
new_record_arr=np.array(new_record)
print(type(new_record))

#Concatenating the new record to the existing numpy array
census=np.concatenate((data,new_record_arr))
print(census.shape)

#1 Analysis of the age distribution of people

age=census[:,0]
print(age.shape)

#Finding the max value of age
max_age=np.amax(age)
print("Max Age= ", max_age)

#Find the min value of age
min_age=np.amin(age)
print("Min Age= ", min_age)

#Find the mean of age
age_mean=np.mean(age)
print("Age Average= ", age_mean)

#Find the standard deviation of age
age_std=np.std(age)
print("Age Standard Deviation= ", age_std)

#2 Checking the country's race distribution to identify the minorities
#  so that the government can help them.

#Creating new subsets based on 'Age'
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]


#Finding the length of the above created subsets
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

#Printing the length of the above created subsets
print('Race_0: ', len_0)
print('Race_1: ', len_1)
print('Race_2: ', len_2)
print('Race_3: ', len_3)
print('Race_4: ', len_4)

#Storing the different race lengths with appropriate indexes
race_list=[len_0, len_1,len_2, len_3, len_4]

#Storing the race with minimum length into a variable 
minority_race=race_list.index(min(race_list))
print(minority_race)

#minority_race is 3, the government can help them.

#3 As per the new govt. policy, all citizens above age 60
#  should not be made to work more than 25 hours per week.
#  Checking if policy is followed?

#Subsetting the array based on the age >60
senior_citizens=census[census[:,0]>60]
print(senior_citizens.shape)

#Calculating the sum of all the values of array
working_hours_sum=senior_citizens[:,6].sum()
print(working_hours_sum)

#Finding the length of the array
senior_citizens_len=len(senior_citizens)

#Finding the average working hours
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)

#avg_working_hours of the senior citizens = 31.42
#No, Policy is not  followed

#4 Checking whether the higher educated people have better pay

#Creating an array based on 'education'>10  
high=census[census[:,1]>10]

#Finding the average pay
avg_pay_high=high[:,7].mean()
print(avg_pay_high)

#Creating an array based on 'education'<=10 
low=census[census[:,1]<=10]

#Finding the average pay
avg_pay_low=low[:,7].mean()
print(avg_pay_low)

# avg_pay_high = 0.43
# avg_pay_low = 0.14
# Educated people have high pay in general




