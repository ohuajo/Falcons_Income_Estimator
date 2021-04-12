# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 13:37:21 2021


"""

#from sklearn.preprocessing import OrdinalEncoder
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




df_columns = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','income']

df_columns_categorical = ['workclass','education','marital-status','occupation','relationship','race','sex','native-country','income']
df_columns_categorical_index = [1,3,5,6,7,8,9,13,14]


df_Adult_Data_File = pd.read_csv('adult.data')

df_Adult_Data_File.columns = df_columns

#print(df_Adult_Data_File.head())

varList_Dictionary_categorical = []

varFactor = 0
###################################
#  loop through category column array here
for cat_column in df_columns_categorical_index:

    column_index = cat_column
    
    ###################################
    #  loop through column variable here
    i = 1
    varDict_Class = {}
    for index, row in df_Adult_Data_File.iterrows():
        #if index > 10:
        #    break
        #print(row[1].strip())
        varCat = row[column_index].strip()
        #print(varCat)
        
        if varCat not in varDict_Class:
            varDict_Class[varCat] = i + varFactor
            i = i + 1
        
        
    
    print(i - 1)
    print(varDict_Class)
    
    varList_Dictionary_categorical.append(varDict_Class)
    varFactor = varFactor + 0


print()
print()
print()
print(varList_Dictionary_categorical)


###################################
# iterate through df here to adjust values to numerical
varNewList = []
for index, row in df_Adult_Data_File.iterrows():
    j = 0
    varNewRow = []
    for intColumn in range(0,15):
        if intColumn in df_columns_categorical_index:
            # convert category to numeric here
            varCat = row[intColumn].strip()
            varNumeric = varList_Dictionary_categorical[j][varCat]
            varNewRow.append(varNumeric)
            j = j + 1
        else:
            # already numeric variable:
            varNumericColumnData = row[intColumn]
            varNewRow.append(varNumericColumnData)
    
    varNewList.append(varNewRow)

print(varNewList[:10])

varDataFrameNumeric = pd.DataFrame(varNewList)
            
#plt.matshow(varDataFrameNumeric.corr())
#plt.show()         

f = plt.figure(figsize=(19, 15))

corr = varDataFrameNumeric.corr()
corr.style.background_gradient(cmap='coolwarm', axis=None)
#corr.style.background_gradient(cmap='coolwarm')

#fig, ax = plt.subplots()

plt.matshow(corr, fignum=f.number)
#plt.matshow(corr)

plt.xticks(range(varDataFrameNumeric.shape[1]), df_columns, fontsize=14, rotation=45)
plt.yticks(range(varDataFrameNumeric.shape[1]), df_columns, fontsize=14)

#for (i, j), z in np.ndenumerate(corr):
#    ax.text(j, i, '{:0.1f}'.format(z), ha='center', va='center')

#plt.xticks(range(varDataFrameNumeric.select_dtypes(['number']).shape[1]), varDataFrameNumeric.select_dtypes(['number']).columns, fontsize=14, rotation=90)
#plt.yticks(range(varDataFrameNumeric.select_dtypes(['number']).shape[1]), varDataFrameNumeric.select_dtypes(['number']).columns, fontsize=14)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
#ax.set_yticklabels(vegetables)
plt.title('Correlation Matrix', fontsize=24, pad=100)

print()
print()
print()
print(corr)
print(corr[14])
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            