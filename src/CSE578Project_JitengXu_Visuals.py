#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv("readonly/adult.txt", header=None, sep=", ")
df.columns = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "class"]
df = df[df["workclass"] != '?']
df = df[df["education"] != '?']
df = df[df["marital-status"] != '?']
df = df[df["occupation"] != '?']
df = df[df["relationship"] != '?']
df = df[df["race"] != '?']
df = df[df["sex"] != '?']
df = df[df["native-country"] != '?']

below = df[df["class"] == "<=50K"]
above = df[df["class"] == ">50K"]
print("Count(Above 50K) = " + str(len(above.index)))
print("Count(Below 50K) = " + str(len(below.index)))

df.head()


# In[2]:


def analyze_numerical_data(column):
    above_50k = list(above[column])
    below_50k = list(below[column])
    
    print(column)
    print()
    print("Mean")
    print("Above 50K = " + str(np.mean(above_50k)))
    print("Below 50K = " + str(np.mean(below_50k)))
    print()
    print("Median")
    print("Above 50K = " + str(np.median(above_50k)))
    print("Below 50K = " + str(np.median(below_50k)))
    print()
    print("Standard Deviation")
    print("Above 50K = " + str(np.std(above_50k)))
    print("Below 50K = " + str(np.std(below_50k)))

    plt.close()
    fig, axes = plt.subplots(ncols=2, nrows=2, figsize=(10,10))
    fig.subplots_adjust(hspace=.5)
    
    axes[0, 0].boxplot(above_50k)
    axes[0, 0].set_title(">50K")
    axes[0, 0].set_xlabel(column)
    
    axes[0, 1].boxplot(below_50k)
    axes[0, 1].set_title("<=50K")
    axes[0, 1].set_xlabel(column)
    
    axes[1, 0].hist(above_50k)
    axes[1, 0].set_title(">50K")
    axes[1, 0].set_xlabel(column)
    
    axes[1, 1].hist(below_50k)
    axes[1, 1].set_title("<=50K")
    axes[1, 1].set_xlabel(column)
    
    plt.show()
    

def analyze_categorical_data(column):
    above_50k = Counter(above[column])
    below_50k = Counter(below[column])

    print(column)
    print()
    plt.close()
    fig, axes = plt.subplots(ncols=1, nrows=2, figsize=(5,10))
    axes[0].pie(above_50k.values(), labels=above_50k.keys(), autopct='%1.0f%%')
    axes[0].set_title(">50K")
    axes[1].pie(below_50k.values(), labels=below_50k.keys(), autopct='%1.0f%%')
    axes[1].set_title("<=50K")
    plt.show()
    
    
def analyze_per_unique_value(column):
    unique_values = df[column].unique()
    plt.close()
    fig, axes = plt.subplots(ncols=1, nrows=len(unique_values), figsize=(5,5 * len(unique_values)))

    for i, val in enumerate(unique_values):
        val_df = df[df[column] == val]
        above_50k = val_df[val_df["class"] == ">50K"]
        below_50k = val_df[val_df["class"] == "<=50K"]
        axes[i].pie([len(below_50k.index), len(above_50k.index)], labels=["<=50K (Count-" + str(len(below_50k.index)) + ")", ">50K (Count-" + str(len(above_50k.index)) + ")"], autopct='%1.0f%%')
        axes[i].set_title(val)
    
    plt.show()


# In[5]:


analyze_numerical_data("hours-per-week")


# In[14]:


analyze_numerical_data("fnlwgt")


# In[ ]:




