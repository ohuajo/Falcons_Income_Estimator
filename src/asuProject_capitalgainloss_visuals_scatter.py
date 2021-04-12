# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:31:12 2021


"""




import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




df_columns = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','income']

df_columns_categorical = ['workclass','education','marital-status','occupation','relationship','race','sex','native-country','income']
df_columns_categorical_index = [1,3,5,6,7,8,9,13,14]


df_Adult_Data_File = pd.read_csv('adult.data', header=None)

df_Adult_Data_File.columns = df_columns

#print(df_Adult_Data_File.head())

varList_Dictionary_categorical = []

########################
########################
########################
########################
########################
######################## build main data frame here for general use for all column variables

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
print()
print()
print()
#print("Numerical List")
#print(varNewList[:10])

varDataFrameNumeric = pd.DataFrame(varNewList)

#print(varDataFrameNumeric)

########################
########################
########################
########################
########################
######################## try scatter plot here  (currently not used for this assignment)

varDataFrameNumeric_capital_gainloss = varDataFrameNumeric.loc[:, [10,11,14]]

varDataFrameNumeric_capital_gainloss_clean = varDataFrameNumeric_capital_gainloss.loc[:, [10,11]]

#print(varDataFrameNumeric_capital_gainloss.head(50))

varDataFrameNumeric_capital_gainloss_less50 = varDataFrameNumeric_capital_gainloss.loc[varDataFrameNumeric_capital_gainloss[14] == 1]
varDataFrameNumeric_capital_gainloss_less50 = varDataFrameNumeric_capital_gainloss_less50.loc[:, [10,11]]
varDataFrameNumeric_capital_gainloss_less50 = varDataFrameNumeric_capital_gainloss_less50.replace(0, np.nan)
varDataFrameNumeric_capital_gainloss_less50 = varDataFrameNumeric_capital_gainloss_less50.dropna(how='all', axis=0)
varDataFrameNumeric_capital_gainloss_less50 = varDataFrameNumeric_capital_gainloss_less50.replace(np.nan, 0)
#varDataFrameNumeric_capital_gainloss_less50 = varDataFrameNumeric_capital_gainloss_less50.reset_index(drop=True)

#print(varDataFrameNumeric_capital_gainloss_less50.head(50))

varDataFrameNumeric_capital_gainloss_greater50 = varDataFrameNumeric_capital_gainloss.loc[varDataFrameNumeric_capital_gainloss[14] == 2]
varDataFrameNumeric_capital_gainloss_greater50 = varDataFrameNumeric_capital_gainloss_greater50.loc[:, [10,11]]
varDataFrameNumeric_capital_gainloss_greater50 = varDataFrameNumeric_capital_gainloss_greater50.replace(0, np.nan)
varDataFrameNumeric_capital_gainloss_greater50 = varDataFrameNumeric_capital_gainloss_greater50.dropna(how='all', axis=0)
varDataFrameNumeric_capital_gainloss_greater50 = varDataFrameNumeric_capital_gainloss_greater50.replace(np.nan, 0)
#varDataFrameNumeric_capital_gainloss_greater50 = varDataFrameNumeric_capital_gainloss_greater50.reset_index(drop=True)

#print(varDataFrameNumeric_capital_gainloss_greater50.head(50))

y1 = varDataFrameNumeric_capital_gainloss_clean[10]
x1 = varDataFrameNumeric_capital_gainloss_clean.index

y2 = varDataFrameNumeric_capital_gainloss_clean[11]
x2 = varDataFrameNumeric_capital_gainloss_clean.index

fig2, ax2 = plt.subplots(1,1)
fig2.set_size_inches(25,25)

ax2.scatter(x1, y1, c='b', label='capital-gain')
ax2.scatter(x2, y2, c='r', label='capital-loss')

#ax2.show()

ax2.legend(loc='best',fontsize=20)

ax2.set_title('Capital Gain, Loss (Population)', fontsize=30)
ax2.set_xlabel("number", fontsize=30)
ax2.set_ylabel("USD $", fontsize=30)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)