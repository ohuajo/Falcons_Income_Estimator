#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
headers = ["age", "workclass","fnwlgt","education","education-num","marital-status","occupation","relationship","race", "sex","capital-gain","capital-loss","hours-per-week","native-country","income"]
data = pd.read_csv("adult.data.csv", names = headers) 
newdata = data[['occupation', 'income']]
newdata.head()
category = [ '?',
            'Adm-clerical',
            'Armed-Forces',
            'Craft-repair',
            'Exec-managerial',
            'Farming-fishing',
            'Handlers-cleaners',
            'Machine-op-inspct',
            'Other-service',
            'Priv-house-serv',
            'Prof-specialty',
            'Protective-serv',
            'Tech-support',
            'Sales', 
            'Transport-moving']

group_50K = newdata[newdata['income'] ==' >50K'].groupby('occupation').count()
lessthan_50K = newdata[newdata['income']==' <=50K'].groupby('occupation').count()


########################################################################################
########################################################################################

x = np.arange(len(category))  # the label locations
width = 0.4  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.barh( x - width/2, group_50K['income'], width, label='Above 50K')
rects2 = ax.barh( x + width/2, lessthan_50K['income'], width, label='Less than 50K')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_title('Income by Occupation')
ax.set_xlabel('Income Count')
ax.set_ylabel('Occupation')
ax.set_yticks(x)
ax.set_yticklabels(category)
ax.legend()

#ax.bar_label(rects1, padding=1)
#ax.bar_label(rects2, padding=1)

fig.tight_layout()
plt.xticks(rotation = 90)
plt.show()


# In[ ]:





# In[ ]:





# In[3]:


print(group_50K)


# In[2]:


headers = ["age", "workclass","fnwlgt","education","education-num","marital-status","occupation","relationship","race", "sex","capital-gain","capital-loss","hours-per-week","native-country","income"]
data = pd.read_csv("adult.data.csv", names = headers) 
newdata = data[['relationship', 'income']]
newdata.head()
category = [ 'Wife',
            'Own-child',
            'Husband', 
            'Not-in-family',
            'Other-relative',
            'Unmarried']

newgroup_50K = newdata[newdata['income'] ==' >50K'].groupby('relationship').count()
newlessthan_50K = newdata[newdata['income']==' <=50K'].groupby('relationship').count()


########################################################################################
########################################################################################

x = np.arange(len(category))  # the label locations
width = 0.4  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar( x - width/2, newgroup_50K['income'], width, label='Above 50K')
rects2 = ax.bar( x + width/2, newlessthan_50K['income'], width, label='Less than 50K')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Relationship')
ax.set_ylabel('Income Count')
ax.set_title('Income by relationship')
ax.set_xticks(x)
ax.set_xticklabels(category)
ax.legend()

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.xticks(rotation = 90)
plt.show()


# In[ ]:





# In[ ]:




