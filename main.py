import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

path = "raw_data"

fields = ['Market_and_Exchange_Names',
          'Report_Date_as_MM_DD_YYYY',
          'Pct_of_OI_Tot_Rept_Long_All',
          'Pct_of_OI_Tot_Rept_Short_All']

asset = {"CAD": "CANADIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE"}

years = ['2022', '2021', '2020', '2019', '2018', '2017', '2006_2016']

columns = ["Date", "OI_LONG", "OI_SHORT"]


def getAssetSpecificCOT(asset, year):
    # variables to obtain from filtered data set
    date = []
    oi_long = []
    oi_short = []

    cot_specific = pd.read_excel(f'{path}/{year}.xls', index_col=0, usecols=fields, dayfirst=True)

    cot_specific = cot_specific.rename(columns={
        'Market_and_Exchange_Names': 'Market',
        'Report_Date_as_MM_DD_YYYY': 'Date',
        'Pct_of_OI_Tot_Rept_Long_All': 'OI_LONG',
        'Pct_of_OI_Tot_Rept_Short_All': 'OI_SHORT'})

    # iterate sample and store data in local
    for index, row in cot_specific.loc[asset].iterrows():
        date.append(row.loc["Date"])
        oi_long.append(row.loc["OI_LONG"])
        oi_short.append(row.loc["OI_SHORT"])

    specificCOTAsset = pd.DataFrame(list(zip(date, oi_long, oi_short)), columns=columns)
    return specificCOTAsset


def getAllYears(asset):
    for year in years:
        df = pd.concat([getAssetSpecificCOT(asset, year)])
    return df


def displaySpecificAsset(df):
    plt.plot(df['Date'], df['OI_LONG'])
    plt.title('Open Interest Long (%)')
    plt.xlabel('Date')
    plt.ylabel('OI_Long')
    plt.show()


combinedDF = getAllYears(asset["CAD"])
displaySpecificAsset(combinedDF)