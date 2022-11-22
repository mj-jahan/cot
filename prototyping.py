'''
Script to load COT data and graph it in a comprehensible way,
such that it can be used during analysis phase.
'''

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

path = "raw_data"

fields = ['Market_and_Exchange_Names',
          'Report_Date_as_MM_DD_YYYY',
          'Pct_of_OI_Tot_Rept_Long_All',
          'Pct_of_OI_Tot_Rept_Short_All']

CFTC_CAD = "CANADIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE"
year = 2020

# variables to obtain from filtered data set
cad_date = []
cad_oi_long = []
cad_oi_short = []
columns = ["Date", "OI_LONG", "OI_SHORT"]


def getAssetSpecificCOT():
    cot_specific = pd.read_excel(f'{path}/{year}.xls', index_col=0, usecols=fields, dayfirst=True)

    cot_specific = cot_specific.rename(columns={
        'Market_and_Exchange_Names': 'Market',
        'Report_Date_as_MM_DD_YYYY': 'Date',
        'Pct_of_OI_Tot_Rept_Long_All': 'OI_LONG',
        'Pct_of_OI_Tot_Rept_Short_All': 'OI_SHORT'})

    cadLen = len(cot_specific.loc[CFTC_CAD]['Date'])  # length of dataset to work with later

    # iterate sample and store data in local
    for index, row in cot_specific.loc[CFTC_CAD].iterrows():
        cad_date.append(row.loc["Date"])
        cad_oi_long.append(row.loc["OI_LONG"])
        cad_oi_short.append(row.loc["OI_SHORT"])

    CAD_DATA = pd.DataFrame(list(zip(cad_date, cad_oi_long, cad_oi_short)), columns=columns)
    return CAD_DATA


def displaySpecificAsset():
    plt.plot(CAD_DATA['Date'], CAD_DATA['OI_LONG'])
    plt.title('Open Interest Long (%)')
    plt.xlabel('Date')
    plt.ylabel('OI_Long')
    plt.show()


CAD_DATA = getAssetSpecificCOT()
displaySpecificAsset()


