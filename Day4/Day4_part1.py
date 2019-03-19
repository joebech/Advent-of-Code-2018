import re
import numpy as np
import pandas as pd
import sys

# Panda settings
pd.set_option('display.max_columns', 65)

# Load input file
df = pd.read_csv('input.dat', names=['a', 'Event'], sep='] ', engine='python')

# Clean and split
df['a'] = df['a'].str.replace("\[", "")
df['Date'], df['Time'] = df['a'].str.split(' ', 1).str
df = df.drop('a', axis=1)
df = df[['Date', 'Time', 'Event']]

# Sorting
df.sort_values(by=['Date', 'Time'],inplace=True)

columns = ['Shift', 'ID'] + list(range(0,60))
sleep = pd.DataFrame(columns=columns)
i = -1

for index, row in df.iterrows():
    if row["Event"][0] == 'G':
        i += 1
        # Shift no
        shift = i + 1
        # Find ID
        new_id = re.findall(r'\d+',row["Event"])
        new_row = [shift] + new_id + list(np.zeros(60, dtype=int))
        sleep.loc[i] = new_row
                
    elif row["Event"][0] == 'f':
        minute = re.findall(r':(\d+)',row["Time"])
        minute = [int(i) for i in minute]
        start = minute[0] + 2
        sleep.loc[i, start:61] = 1

    elif row["Event"][0] == 'w':
        minute = re.findall(r':(\d+)',row["Time"])
        minute = [int(i) for i in minute]
        start = minute[0] + 2
        sleep.loc[i, start:61] = 0


# Who sleeps the most
col_list= list(sleep)
col_list.remove('ID')
col_list.remove('Shift')
sleep['Total'] = sleep[col_list].sum(axis=1)

#print('Who sleeps the most:')
#print(sleep.groupby(['ID']).sum())

# What minute is Guard # XX sleeping most?

sleeppattern = sleep.loc[sleep['ID'] == '499']
sleeppattern.loc['Totalrow']= sleeppattern.sum()
#print(sleeppattern)

# Part 2
table = pd.pivot_table(sleep, values=list(range(0,60)),columns=['ID'], aggfunc=np.sum)
print(table)
