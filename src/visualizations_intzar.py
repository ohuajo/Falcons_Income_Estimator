# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 


# %%
headers = ["age",
               "workingclass",
               "fnlwgt",
               "education",
               "education_num",
               "marital_status",
               "occupation",
               "relationship",
               "race",
               "sex",
               "capital_gain",
               "capital_loss",
               "hours_per_week",
               "native_country",
               "income"]
data = pd.read_csv('/Users/intzar/Downloads/adult.data', names = headers)


# %%
# Getting a Peek into the data 
data


# %%
# Shape of the table
print('Max Value of Education-Num:', data['education_num'].max())
print('Min Value of Education-Num:',data['education_num'].min())
new_data1 = data[['education_num','income']]
#new_data1.dropna()
new_data1


# %%
# I want to create a box plot with categories 

#print(new_data1['income'].unique())

income_less50k = new_data1[new_data1['income'] ==' <=50K']
income_greater50k = new_data1[new_data1['income'] == ' >50K']

income_greater50k = income_greater50k['education_num'].to_numpy()
income_less50k = income_less50k['education_num'].to_numpy()



fig,(ax1,ax2)  = plt.subplots(nrows=1, ncols=2, figsize = (9,4))

bplot1 = ax1.boxplot(income_greater50k,
                     vert=True, 
                     patch_artist=True,  
                     labels=['Education Level'])
ax1.set_title('Income Greater than 50k')
ax1.set_ylabel('Education Level')

bplot2 = ax2.boxplot(income_less50k,
                     vert=True,  
                     patch_artist=True, 
                     labels=['Education Level'])                     
ax2.set_title('Income Less than 50k')
ax2.set_ylabel('Education Level')





# %%
combined_data = [income_greater50k,income_less50k]

box = plt.boxplot(combined_data,
                     vert=True, 
                     patch_artist=True,  
                     labels=['>50k','<50k'],
                     widths= .60, showfliers= False
                     )
plt.title('Education Distribution to Income Level')
plt.ylabel('Education Level')

colors = ['green', 'green']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

colors = ['red','red']
for patch, color in zip(box['medians'], colors):
    patch.set_color(color)


plt.show()


# %%
new_data2 = data[['marital_status','income']]
new_data2.head()
category_list = ['Divorced',
 'Married-AF-spouse',
 'Married-civ-spouse',
 'Married-spouse-absent',
 'Never-married',            
 'Separated',                
 'Widowed']

grouped_data_incomegreater50k = new_data2[new_data2['income'] == ' >50K'].groupby('marital_status').count()
grouped_data_incomeless50k = new_data2[new_data2['income'] == ' <=50K'].groupby('marital_status').count()

plt.bar(category_list,grouped_data_incomegreater50k['income'], width =.6, align = 'center', label = 'Greater Than 50K', color = 'g')
plt.bar(category_list,grouped_data_incomeless50k['income'], bottom = grouped_data_incomegreater50k['income'], width =.6, align = 'center', color = 'r',label = 'Less Than 50K')
plt.xlabel('Marital Status')
plt.ylabel('# of People')
plt.legend()

plt.xticks(rotation = 90)


# %%



# %%



