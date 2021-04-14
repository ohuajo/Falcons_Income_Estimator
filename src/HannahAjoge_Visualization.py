#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px
from scipy import stats
from geonamescache.mappers import country
import os


# In[2]:


# Read the main data into jupyter notebook
df_data = pd.read_csv("adult.data", header=None)
# View the first 5 rows
df_data.head()
# View the main data dimensions 
df_data.shape
#Check for breakdown of income
df_data[14].unique()
#Subset by income
df_g50k = df_data[df_data[14] == " >50K"]
df_l50k = df_data[df_data[14] == " <=50K"]
df_g50k.head()
df_l50k.head()


# In[3]:


# Read and view the adult.names content
with open('adult.names') as f:
    for lines in f:
        print(lines)


# In[4]:


# chisquare test for sex
income_sex = pd.crosstab(index=df_data[14], columns=df_data[9])
(chi2, p, dof,_) = stats.chi2_contingency([income_sex.iloc[0].values, income_sex.iloc[1].values])
print(p)
print(chi2)
print(dof)


# In[5]:


# chisquare test for race
income_race = pd.crosstab(index=df_data[14], columns=df_data[8])
(chi2, p, dof,_) = stats.chi2_contingency([income_race.iloc[0].values, income_race.iloc[1].values])
print(p)
print(chi2)
print(dof)


# In[6]:


# SEX

#pd.set_option("max_columns", 30)
l_inc_sex = df_l50k.loc[:, [14,9]]
g_inc_sex = df_g50k.loc[:, [14,9]]
lpercent = l_inc_sex.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
lpercent_male =lpercent[0]
lpercent_male = "Male ("+ lpercent_male + " of <=50K)"
lpercent_female =lpercent[1]
lpercent_female = "Female ("+ lpercent_female + " of <=50K)"
gpercent = g_inc_sex.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
gpercent_male =gpercent[0]
gpercent_male = "Male ("+ gpercent_male + " of >50K)"
gpercent_female =gpercent[1]
gpercent_female  = "Female ("+ gpercent_female + " of >50K)"

def label_sex (row):
   if row[14] == " >50K" and row[9] == ' Male':
      return gpercent_male
   if row[14] == " >50K" and row[9] == ' Female':
      return gpercent_female
   if row[14] == " <=50K" and row[9] == ' Male':
      return lpercent_male
   return lpercent_female

df_data['sex_label'] = df_data.apply (lambda row: label_sex(row), axis=1)

df_data['sex_p_value'] = "p<0.05"

fig = px.sunburst(df_data,
                  path=['sex_p_value', 14, 'sex_label',],
                  width=800, height=800,
                  title="Distribution of Income by Sex",
                  )
fig.show()


# In[7]:


# RACE

#unique components of race
df_data[8].unique()

l_inc_race = df_l50k.loc[:, [14,8]]
g_inc_race = df_g50k.loc[:, [14,8]]
lpercent = l_inc_race.value_counts()
lrace_count = [lpercent[3], lpercent[2], lpercent[1], lpercent[4], lpercent[0]]
gpercent = g_inc_race.value_counts()
grace_count = [gpercent[3], gpercent[2], gpercent[1], gpercent[4], gpercent[0]]
race = ['Amer-Indian-Eskimo', 'Asian-Pac-Islander','Black', 
       'Other', 'White']

explode = [0,0.1,0,0,0.1]

plt.figure(figsize = (17,8))
plt.subplot(1,2,1)
plt.title('Distribution of Income less than or equal to 50K by Race')
plt.pie(lrace_count, labels=race, explode = explode, autopct='%2.1f%%')
plt.subplot(1,2,2)
plt.title('Distribution of Income greater than 50K by Race')
plt.pie(grace_count, labels=race, explode = explode, autopct='%2.1f%%')
plt.show()


# In[8]:


# NATIVE COUNTRY
mapper = country(from_key='name', to_key='iso3')
# This function is adopted and modified from 
# https://melaniesoek0120.medium.com/data-visualization-how-to-plot-a-map-with-geopandas-in-python-73b10dcd4b4b
# generate country code  based on country name 
def alpha3code(column):
    CODE=[]
    for country in column:
        try:
            iso3 = mapper(country)
            CODE.append(iso3)
        except:
            CODE.append('None')
    return CODE

# create a column for code 
df_data[13] = df_data[13].str.replace(' ', '')
df_data[13] = df_data[13].str.replace('United-States', 'United States')
df_data[13] = df_data[13].str.replace('Puerto-Rico', 'Puerto Rico')
df_data[13] = df_data[13].str.replace('Dominican-Republic', 'Dominican Republic')
df_data[13] = df_data[13].str.replace('El-Salvador', 'El Salvador')
df_data[13] = df_data[13].str.replace('Trinadad&Tobago', 'Trinidad and Tobago')
df_data[13] = df_data[13].str.replace('Holand-Netherlands', 'Netherlands')
df_data[13] = df_data[13].str.replace('Hong', 'Hong Kong')
df_data[13] = df_data[13].str.replace('Scotland', 'United Kingdom')
df_data[13] = df_data[13].str.replace('Outlying-US\(Guam-USVI-etc\)', 'United States')
df_data[13] = df_data[13].str.replace('Columbia', 'Colombia')
df_data['CODE']=alpha3code(df_data[13])
#df_data.to_excel("manData.xlsx")
#df_None= df_data[df_data['CODE'] == "None"]
df_l50k = df_data[df_data[14] == " <=50K"]
df_g50k = df_data[df_data[14] == " >50K"]
df_geol =  df_l50k.loc[:, [13,'CODE']]
df_geol.columns = ['country', 'code']
df_geog =  df_g50k.loc[:, [13,'CODE']]
df_geog.columns = ['country', 'code']

df_geol = (df_geol.fillna('')      .groupby(df_geol.columns.tolist()).apply(len)      .rename('group_count')      .reset_index()      .replace('',np.nan)      .sort_values(by = ['group_count'], ascending = False))

df_geog = (df_geog.fillna('')      .groupby(df_geog.columns.tolist()).apply(len)      .rename('group_count')      .reset_index()      .replace('',np.nan)      .sort_values(by = ['group_count'], ascending = False))
lpercent = df_geol['group_count'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
gpercent = df_geog['group_count'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'

shapefile = gpd.read_file(os.path.expanduser('shapeFiles/ne_10m_admin_0_countries.shp'))[['ADM0_A3', 'geometry']].to_crs('+proj=robin')

shapefile2 = gpd.read_file(os.path.expanduser('shapeFiles/ne_10m_admin_0_countries.shp'))[['ADMIN','ADM0_A3', 'geometry']].to_crs('+proj=robin')
shapefile3 = pd.DataFrame([shapefile2['ADMIN'],shapefile2['ADM0_A3']])
shapefile3 = shapefile3.transpose()
shapefile3.columns = ['country', 'code']
shapefile3['group_count'] = 0
llist = df_geol['code'].tolist()
lnot = shapefile3[~shapefile3.code.isin(llist)]
glist = df_geog['code'].tolist()
gnot = shapefile3[~shapefile3.code.isin(glist)]

df_geol = pd.concat([df_geol, lnot], ignore_index=True)
df_geog = pd.concat([df_geog, gnot], ignore_index=True)

mergedl = shapefile.merge(df_geol, left_on='ADM0_A3', right_on='code')
mergedg = shapefile.merge(df_geog, left_on='ADM0_A3', right_on='code')


plt.rcParams["figure.figsize"]=20,20

# Distribution of Income less than or equal to 50K by Native Country
mergedl['centroid_column'] = mergedl.centroid
centroids1 = list(mergedl['centroid_column'])
df1 = pd.DataFrame({'y':[centroids1[i].y for i in range(len(centroids1))], 'x':[centroids1[i].x for i in range(len(centroids1))], 'data1':list(mergedl['group_count'])})
base1 = mergedl.plot(color='white', edgecolor='grey')
df1.plot( kind='scatter', x='x', y='y', s=df1['data1']*0.5, ax=base1, color='red')

# Distribution of Income greater than to 50K by Native Country
mergedg['centroid_column'] = mergedg.centroid
centroids = list(mergedg['centroid_column'])
df = pd.DataFrame({'y':[centroids[i].y for i in range(len(centroids))], 'x':[centroids[i].x for i in range(len(centroids))], 'data':list(mergedg['group_count'])})
base = mergedg.plot(color='white', edgecolor='grey')
df.plot( kind='scatter', x='x', y='y', s=df['data']*0.5, ax=base, color='red')

plt.show()

