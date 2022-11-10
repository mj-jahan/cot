# Shift+F10 to execute it or replace it with your code.
# Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint to debug your script.
# Press Ctrl+F8 to toggle the breakpoint.

'''
Script to load COT data and graph it in a comprehensible way,
such that it can be used during analysis phase.
'''

import pandas as pd
import numpy as np

path = "raw_data"

date_col = 'Report_Date_as_MM_DD_YYYY'

fields = ['Market_and_Exchange_Names',
          'Report_Date_as_MM_DD_YYYY',
          'Pct_of_OI_Tot_Rept_Long_All',
          'Pct_of_OI_Tot_Rept_Short_All']


CFTC_CAD = "CANADIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE"
year = 2020

data_2020 = pd.read_excel(f'{path}/{year}.xls', index_col=0, usecols=fields, dayfirst=True)

data_2020 = data_2020.rename(columns={
    'Market_and_Exchange_Names': 'Market',
    'Report_Date_as_MM_DD_YYYY': 'Date',
    'Pct_of_OI_Tot_Rept_Long_All': 'OI_LONG',
    'Pct_of_OI_Tot_Rept_Short_All': 'OI_SHORT'})

cadLen = len(data_2020.loc[CFTC_CAD]['Date'])  # length of dataset to work with later

# variables to obtain from filtered data set
cad_date = []
cad_oi_long = []
cad_oi_short = []

# iterate sample and store data in local
for index, row in data_2020.loc[CFTC_CAD].iterrows():
    cad_date.append(row.loc["Date"])
    cad_oi_long.append(row.loc["OI_LONG"])
    cad_oi_short.append(row.loc["OI_SHORT"])

columns = ["Date", "OI_LONG", "OI_SHORT"]
CAD_DATA = pd.DataFrame(list(zip(cad_date, cad_oi_long, cad_oi_short)), columns=columns)

print(CAD_DATA)
