# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
print("\nData: \n\n", data)

print("\nType of data: \n\n", type(data))
print(data.shape)
new_record_arr=np.array(new_record)
print(type(new_record))

census=np.concatenate((data,new_record_arr))
print(census.shape)
print(type(census))

#Step 2
age=census[:,0]
print(age.shape)
print(type(age))

max_age=np.amax(age)
print(max_age)

min_age=np.amin(age)
print(min_age)

age_mean=np.mean(age)
print(age_mean)

age_std=np.std(age)
print(age_std)

# Step 3

race=census[:,2]
print(race.shape)

race_0=race[race == 0]
len_0=len(race_0)
print(len_0)

race_1=race[race == 1]
len_1=len(race_1)
print(len_1)

race_2=race[race == 2]
len_2=len(race_2)
print(len_2)

race_3=race[race == 3]
len_3=len(race_3)
print(len_3)

race_4=race[race == 4]
len_4=len(race_4)
print(len_4)

minority_race=3

#Step 4

senior_citizens=census[census[:,0]>60]
print(senior_citizens.shape)

working_hours_sum=senior_citizens[:,6].sum()
print(working_hours_sum)

senior_citizens_len=len(senior_citizens)

avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)

#Step 5

high=census[census[:,1]>10]
low=census[census[:,1]<=10]

avg_pay_high=high[:,7].mean()
print(avg_pay_high)

avg_pay_low=low[:,7].mean()
print(avg_pay_low)







