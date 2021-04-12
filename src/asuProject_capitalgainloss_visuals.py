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

#y1 = varDataFrameNumeric_capital_gainloss_clean[10]
#x1 = varDataFrameNumeric_capital_gainloss_clean.index

#y2 = varDataFrameNumeric_capital_gainloss_clean[11]
#x2 = varDataFrameNumeric_capital_gainloss_clean.index

#fig2, ax2 = plt.subplots(1,1)
#fig2.set_size_inches(25,25)

#ax2.scatter(x1, y1, c='b', label='capital-gain')
#ax2.scatter(x2, y2, c='r', label='capital-loss')

#ax2.show()

#ax2.legend(loc='upper left')

#ax2.set_title('Capital Gain, Loss (Population)')
#ax2.set_xlabel("number")
#ax2.set_ylabel("USD $")

#ax2.show()






########################
########################
########################
########################
########################
######################## try pie plot here - for capital gain or loss (total population):


varDataFrameNumeric_less50 = varDataFrameNumeric_capital_gainloss.loc[varDataFrameNumeric_capital_gainloss[14] == 1, [10,11]]
varDataFrameNumeric_less50 = varDataFrameNumeric_less50.replace(0, np.nan)
varDataFrameNumeric_less50 = varDataFrameNumeric_less50.dropna(how='all', axis=0)
varDataFrameNumeric_less50 = varDataFrameNumeric_less50.replace(np.nan, 0)

varDataFrameNumeric_greater50 = varDataFrameNumeric_capital_gainloss.loc[varDataFrameNumeric_capital_gainloss[14] == 2, [10,11]]
varDataFrameNumeric_greater50 = varDataFrameNumeric_greater50.replace(0, np.nan)
varDataFrameNumeric_greater50 = varDataFrameNumeric_greater50.dropna(how='all', axis=0)
varDataFrameNumeric_greater50 = varDataFrameNumeric_greater50.replace(np.nan, 0)


varV1 = len(varDataFrameNumeric_less50)
varV2 = len(varDataFrameNumeric_greater50)

#print()
#print()
#print(varV1)
#print(varV2)

varPercentV1 = varV1 / (varV1 + varV2)
varPercentV2 = varV2 / (varV1 + varV2)

#print(varPercentV1)
#print(varPercentV2)

labels = 'Income <= 50 K', 'Income > 50 K'
sizes = [varPercentV1, varPercentV2]
#colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
colors = ['lightcoral', 'lightskyblue']


# Plot
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=False, startangle=90)

plt.title("Total Capital-Gain or Loss (Population)\n\n", fontsize=30,ha='center')


plt.axis('equal')
plt.show()






########################
########################
########################
########################
########################
######################## try pie chart here

varTotal_pie1_v1 = varDataFrameNumeric_capital_gainloss_less50[10].sum()
varTotal_pie1_v2 = varDataFrameNumeric_capital_gainloss_less50[11].sum()

#print(varTotal_pie1_v1)
#print(varTotal_pie1_v2)

var_Percent_pie1_v1 = varTotal_pie1_v1 / (varTotal_pie1_v1 + varTotal_pie1_v2)
var_Percent_pie1_v2 = varTotal_pie1_v2 / (varTotal_pie1_v1 + varTotal_pie1_v2)

#print(var_Percent_pie1_v1)
#print(var_Percent_pie1_v2)



varTotal_pie2_v1 = varDataFrameNumeric_capital_gainloss_greater50[10].sum()
varTotal_pie2_v2 = varDataFrameNumeric_capital_gainloss_greater50[11].sum()

#print(varTotal_pie2_v1)
#print(varTotal_pie2_v2)

var_Percent_pie2_v1 = varTotal_pie2_v1 / (varTotal_pie2_v1 + varTotal_pie2_v2)
var_Percent_pie2_v2 = varTotal_pie2_v2 / (varTotal_pie2_v1 + varTotal_pie2_v2)

#print(var_Percent_pie2_v1)
#print(var_Percent_pie2_v2)

labels = 'capital-gain', 'capital-loss'
sizes = [var_Percent_pie1_v1, var_Percent_pie1_v2]
#colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
colors = ['lightcoral', 'lightskyblue']


# Plot
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=False, startangle=90)

plt.title("Income <= 50 K:  by Capital-Gain, Loss \n\n", fontsize=30,ha='center')


plt.axis('equal')
plt.show()




print()
print()
print()
print()
print()
print()
print()
print()
print()
print()


labels = 'capital-gain', 'capital-loss'
sizes = [var_Percent_pie2_v1, var_Percent_pie2_v2]
#colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
colors = ['lightcoral', 'lightskyblue']


# Plot
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=False, startangle=90)

plt.title("Income > 50 K:  by Capital-Gain, Loss \n\n", fontsize=30,ha='center')


plt.axis('equal')
plt.show()



print()
print()
print()
print()
print()
print()
print()
print()
print()
print()



########################
########################
########################
########################
########################
######################## try box plot here

var_data1 = varDataFrameNumeric_capital_gainloss_less50[10]
var_data2 = varDataFrameNumeric_capital_gainloss_less50[11]
var_data3 = varDataFrameNumeric_capital_gainloss_greater50[10]
var_data4 = varDataFrameNumeric_capital_gainloss_greater50[11]
fig1, ax1 = plt.subplots(1,4)
fig1.set_size_inches(25,10)
ax1[0].set_title('capital-gain:  <= 50 K',fontsize=20)
ax1[0].set_xlabel("capital-gain:  <= 50 K", rotation=0, size='large')
ax1[0].set_ylabel("USD $", rotation=90, size='large')
ax1[0].boxplot(var_data1)

ax1[1].set_title('capital-loss:  <= 50 K',fontsize=20)
ax1[1].set_xlabel("capital-loss:  <= 50 K", rotation=0, size='large')
ax1[1].set_ylabel("USD $", rotation=90, size='large')
ax1[1].boxplot(var_data2)

ax1[2].set_title('capital-gain:  > 50 K',fontsize=20)
ax1[2].set_xlabel("capital-gain:  > 50 K", rotation=0, size='large')
ax1[2].set_ylabel("USD $", rotation=90, size='large')
ax1[2].boxplot(var_data3)

ax1[3].set_title('capital-loss:  > 50 K',fontsize=20)
ax1[3].set_xlabel("capital-loss:  > 50 K", rotation=0, size='large')
ax1[3].set_ylabel("USD $", rotation=90, size='large')
ax1[3].boxplot(var_data4)

plt.show()


print()
print()
print()
print()
print()
print()
print()
print()
print()
print()



########################
########################
########################
########################
########################
######################## try pie plot here - for education:

varDataFrameNumeric_education = varDataFrameNumeric.loc[:, [4,14]]

#print(varDataFrameNumeric_capital_gainloss.head(50))

varDataFrameNumeric_education_less50 = varDataFrameNumeric_education.loc[varDataFrameNumeric_education[14] == 1]
varDataFrameNumeric_education_less50 = varDataFrameNumeric_education_less50.loc[:, [4]]
varDataFrameNumeric_education_less50 = varDataFrameNumeric_education_less50.replace(0, np.nan)
varDataFrameNumeric_education_less50 = varDataFrameNumeric_education_less50.dropna(how='all', axis=0)
varDataFrameNumeric_education_less50 = varDataFrameNumeric_education_less50.replace(np.nan, 0)
#varDataFrameNumeric_capital_gainloss_less50 = varDataFrameNumeric_capital_gainloss_less50.reset_index(drop=True)

#print(varDataFrameNumeric_education_less50.head(50))

varDataFrameNumeric_education_greater50 = varDataFrameNumeric_education.loc[varDataFrameNumeric_capital_gainloss[14] == 2]
varDataFrameNumeric_education_greater50 = varDataFrameNumeric_education_greater50.loc[:, [4]]
varDataFrameNumeric_education_greater50 = varDataFrameNumeric_education_greater50.replace(0, np.nan)
varDataFrameNumeric_education_greater50 = varDataFrameNumeric_education_greater50.dropna(how='all', axis=0)
varDataFrameNumeric_education_greater50 = varDataFrameNumeric_education_greater50.replace(np.nan, 0)

varV1 = len(varDataFrameNumeric_education_less50)
varV2 = len(varDataFrameNumeric_education_greater50)

varPercentV1 = varV1 / (varV1 + varV2)
varPercentV2 = varV2 / (varV1 + varV2)

#print(varPercentV1)
#print(varPercentV2)

labels = 'Income <= 50 K', 'Income > 50 K'
sizes = [varPercentV1, varPercentV2]
#colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
colors = ['lightcoral', 'lightskyblue']


# Plot
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=False, startangle=90)

plt.title("Total Education (Population)\n\n", fontsize=30,ha='center')


plt.axis('equal')
plt.show()






print()
print()
print()
print()
print()
print()
print()
print()
print()
print()



########################
########################
########################
########################
########################
######################## try pie plot here - for education :  <= 50K

#print(varDataFrameNumeric_education_less50)
varDataFrameNumeric_education_less50_degree = varDataFrameNumeric_education_less50.loc[varDataFrameNumeric_education_less50[4] >= 10]
varDataFrameNumeric_education_less50_degree = varDataFrameNumeric_education_less50_degree.loc[:, [4]]
varDataFrameNumeric_education_less50_degree = varDataFrameNumeric_education_less50_degree.replace(0, np.nan)
varDataFrameNumeric_education_less50_degree = varDataFrameNumeric_education_less50_degree.dropna(how='all', axis=0)
varDataFrameNumeric_education_less50_degree = varDataFrameNumeric_education_less50_degree.replace(np.nan, 0)

varDataFrameNumeric_education_less50_no_degree = varDataFrameNumeric_education_less50.loc[varDataFrameNumeric_education_less50[4] < 10]
varDataFrameNumeric_education_less50_no_degree = varDataFrameNumeric_education_less50_no_degree.loc[:, [4]]
varDataFrameNumeric_education_less50_no_degree = varDataFrameNumeric_education_less50_no_degree.replace(0, np.nan)
varDataFrameNumeric_education_less50_no_degree = varDataFrameNumeric_education_less50_no_degree.dropna(how='all', axis=0)
varDataFrameNumeric_education_less50_no_degree = varDataFrameNumeric_education_less50_no_degree.replace(np.nan, 0)

varV1 = len(varDataFrameNumeric_education_less50_degree)
varV2 = len(varDataFrameNumeric_education_less50_no_degree)

varPercentV1 = varV1 / (varV1 + varV2)
varPercentV2 = varV2 / (varV1 + varV2)

#print(varPercentV1)
#print(varPercentV2)

labels = 'Education Level >= 10', 'Education Level < 10'
sizes = [varPercentV1, varPercentV2]
#colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
colors = ['lightcoral', 'lightskyblue']


# Plot
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=False, startangle=90)

plt.title("Income <= 50 K:  by Education Level \n\n", fontsize=30,ha='center')


plt.axis('equal')
plt.show()







print()
print()
print()
print()
print()
print()
print()
print()
print()
print()



########################
########################
########################
########################
########################
######################## try pie plot here - for education :  > 50K

#print(varDataFrameNumeric_education_less50)
varDataFrameNumeric_education_greater50_degree = varDataFrameNumeric_education_greater50.loc[varDataFrameNumeric_education_greater50[4] >= 10]
varDataFrameNumeric_education_greater50_degree = varDataFrameNumeric_education_greater50_degree.loc[:, [4]]
varDataFrameNumeric_education_greater50_degree = varDataFrameNumeric_education_greater50_degree.replace(0, np.nan)
varDataFrameNumeric_education_greater50_degree = varDataFrameNumeric_education_greater50_degree.dropna(how='all', axis=0)
varDataFrameNumeric_education_greater50_degree = varDataFrameNumeric_education_greater50_degree.replace(np.nan, 0)

varDataFrameNumeric_education_greater50_no_degree = varDataFrameNumeric_education_greater50.loc[varDataFrameNumeric_education_greater50[4] < 10]
varDataFrameNumeric_education_greater50_no_degree = varDataFrameNumeric_education_greater50_no_degree.loc[:, [4]]
varDataFrameNumeric_education_greater50_no_degree = varDataFrameNumeric_education_greater50_no_degree.replace(0, np.nan)
varDataFrameNumeric_education_greater50_no_degree = varDataFrameNumeric_education_greater50_no_degree.dropna(how='all', axis=0)
varDataFrameNumeric_education_greater50_no_degree = varDataFrameNumeric_education_greater50_no_degree.replace(np.nan, 0)

varV1 = len(varDataFrameNumeric_education_greater50_degree)
varV2 = len(varDataFrameNumeric_education_greater50_no_degree)

varPercentV1 = varV1 / (varV1 + varV2)
varPercentV2 = varV2 / (varV1 + varV2)

#print(varPercentV1)
#print(varPercentV2)

labels = 'Education Level >= 10', 'Education Level < 10'
sizes = [varPercentV1, varPercentV2]
#colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
colors = ['lightcoral', 'lightskyblue']


# Plot
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=False, startangle=90)

plt.title("Income > 50 K:  by Education Level \n\n", fontsize=30,ha='center')


plt.axis('equal')
plt.show()

"""
            
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

"""
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            