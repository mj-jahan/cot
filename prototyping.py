# assume all years of cot has been downloaded
import os
import pandas as pd
from datetime import datetime

fields = ['Market_and_Exchange_Names',
          'Report_Date_as_MM_DD_YYYY',
          'Pct_of_OI_Tot_Rept_Long_All',
          'Pct_of_OI_Tot_Rept_Short_All']


def combineSheets():
    cot_year = []
    cot_year = pd.DataFrame()
    path = "raw_data/"

    dir_limit = len((os.listdir(path)))

    years = []
    for i in range(2016, 2023):
        years.append(i)

    print(years)



#    for index, file in enumerate(os.listdir(path)):


#        cot_year = cot_year.append(pd.read_excel(f'{file}', index_col=0, usecols=fields))


def main():
    combineSheets()


main()
# access all excel sheets

# scan for the rows we want only based on column value.
# in descending order = current to end.
