# assume all years of cot has been downloaded
import os
import pandas as pd
from datetime import datetime

fields = ['Market_and_Exchange_Names',
          'Report_Date_as_MM_DD_YYYY',
          'Pct_of_OI_Tot_Rept_Long_All',
          'Pct_of_OI_Tot_Rept_Short_All']

path = 'raw_data'


# check current directory folder.
# if no raw_data folder, create one.
# if raw_data folder, check contents.
def checkDirectory():
    for index, file in enumerate(os.listdir()):
        if path in file:
            scanFiles()


# scan directory for .xls files
# process titles, check if needed to download more
def scanFiles():
    for index, file in enumerate(os.listdir(path)):
        print(f"{index} - {file}")


# download zipped files from cot website
def getData():
    return False


# cot_year = cot_year.append(pd.read_excel(f'{file}', index_col=0, usecols=fields))
def prepareData():
    return False

# if theres files already in there, still go ahead to the website and override.


# create raw_data folder
def makeDirectory():
    print("True")
    return False


def main():
    checkDirectory()


main()
# access all excel sheets

# scan for the rows we want only based on column value.
# in descending order = current to end.
