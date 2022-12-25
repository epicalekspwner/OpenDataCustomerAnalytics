### script_CountryRelative
### Convert Absolute Values Into Relative Ones (Within Country)
### /demographicsData/demographicsHousehold/
### Potential SettingWithCopyWarning Can Be Ignored!

### Import Pandas and OS Libraries
import pandas as pd
import os

### Set Periodicity
periodicity = list(range(2016, 2021))

### Create New Dictionary
dictURL = {}

### Create Corresponding URLs and Store Them in the Dictionary Created Beforehand
for year in periodicity:
    dictURL['{0}'.format(year)] = 'https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsData/demographicsHousehold/' + str(year) + '_demographicsHousehold_Absolute.csv'

### Get the Dictionary Keys to Access the URLs
keys = list(dictURL.keys())

### Create New Dictionary for Storing the DataFrames
dictDataFrames = {}

### Accessing the Original Datasets Through URLs and Converting Them Into DataFrames
for i in range(len(keys)):
    dictDataFrames['{0}'.format(keys[i])] = pd.read_csv(dictURL[keys[i]])

### Get Column Names and Drop Useless Attribute for Relativeness
attr = list(dictDataFrames[keys[0]].columns)
attrToBeRemoved = ['region', 'total', 'averageSizeHousehold']
for i in attrToBeRemoved:
    attr.remove(i)

### Iteration and Convertion Into Percentage (Within Country)
for i in range(len(dictDataFrames)):
    for j in attr:
        for k in range(26):
            dictDataFrames[keys[i]][j][k] = round(dictDataFrames[keys[i]][j][k]/dictDataFrames[keys[i]][j][26], 4)

### Export Data With Automated Files Management
for i in dictDataFrames.keys():
    exportPath = 'C:/GitHub/OpenDataCustomerAnalytics/demographicsData/demographicsHousehold/'
    exportPathExist = os.path.exists(exportPath)
    if not exportPathExist:
        os.makedirs(exportPath)
    exportFile = 'C:/GitHub/OpenDataCustomerAnalytics/demographicsData/demographicsHousehold/{0}_demographicsHousehold_CountryRelative.csv'.format(i)
    dictDataFrames[i].to_csv(exportFile, na_rep = 'NaN', index = False)
