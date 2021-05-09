#Finds the number of buildings in each borough
#Creates a list of indices of buildings in each borough in the raw dataset

import csv, pandas
data = pandas.read_csv('HousingDataRaw.csv',  usecols=['Project Name', 'Program Group', 'Borough', 'Extremely Low Income Units', 'Very Low Income Units', 'Low Income Units', 'Moderate Income Units', 'Total Units'])

mht = data.loc[data['Borough'] == 'Manhattan']
mht_indices = list()
for row in mht.iterrows():
    mht_indices.append(row[0])

brx = data.loc[data['Borough'] == 'Bronx']
brx_indices = list()
for row in brx.iterrows():
    brx_indices.append(row[0])

brk = data.loc[data['Borough'] == 'Brooklyn']
brk_indices = list()
for row in brk.iterrows():
    brk_indices.append(row[0])

sti = data.loc[data['Borough'] == 'Staten Island']
sti_indices = list()
for row in sti.iterrows():
    sti_indices.append(row[0])

qen = data.loc[data['Borough'] == 'Queens']
queen_indices = list()
for row in qen.iterrows():
    queen_indices.append(row[0])

print(f"Number of buildings: \n Manhattan: {len(mht_indices)} \n Bronx: {len(brx_indices)} \n Brooklyn: {len(brk_indices)} \n Staten Island: {len(sti_indices)} \n Queens: {len(queen_indices)}")