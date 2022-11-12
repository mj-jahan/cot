'''
Download COT data
Extract
Ready-to-use in folder.
'''

import requests, zipfile, io, os

path = "raw_data"
URL = "https://www.cftc.gov/files/dea/history/com_fin_xls"
URL06_16 = 'https://www.cftc.gov/files/dea/history/fin_com_xls'
YEAR = ['2022', '2021', '2020', '2019', '2018', '2017', '2006_2016']
YEAR06_16 = '2006_2016'
name = "FinComYY.xls"
name06_16 = "C_TFF_2006_2016.xls"


def dialog(hasDir):
    inputArg = []

    if hasDir:
        if checkDirectoryContents():
            print("folder and files")

    # what files in directory? should update or override directory?

    elif not hasDir:
        print("[1] - Get all data and refresh directory")
        print("[2] - Enter own command line")

        choice = int(input("Enter: "))

        if choice == 1:
            getAllData()
        elif choice == 2:
            print("arguments are: str(url), str(path), str(year), str(name)")
            for i in range(0, 4):
                inputArg.append(input(f"arg[{i}]: "))


# single function that can be looped.
def downloadData(url, path, year, name):
    print(f"Begin {year}.xls")
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(f"{path}/")
    os.rename(f"{path}/{name}", f"{path}/{year}.xls")
    print(f"{year}.xls successful")


# get all current data
def getAllData():
    # all years (separated)
    for year in YEAR:
        if '2006_2016' in year:
            downloadData(f"{URL06_16}_{year}.zip", path, year, name06_16)
        else:
            downloadData(f"{URL}_{year}.zip", path, year, name)


# check if directory has contents
# if directory, access all file names
# if no directory, create one, and fill with getAllData()
def checkDirectory():
    count = 0
    path = "raw_data"
    folder = False
    file_list = []

    for index, file in enumerate(os.listdir()):
        if path in file:
            folder = True

    if folder:
        # has files, gets list of file names from directory
        for index, file in enumerate(os.listdir(path)):
            file_list.append(file[:-4])  # get list of files in directory w/o '.xls'

        # begin folder=TRUE logic

        # if folder, has correct number of contents, print contents
        if len(file_list) == len(YEAR):
            print(file_list)

        # if folder, no files = get all data
        elif len(file_list) == 0:
            getAllData()

        # if folder, some files = get the rest
        elif len(file_list) < len(YEAR):
            get_years = []
            counter = 0

            for year in YEAR:
                print(file_list[counter])
                print(YEAR[counter])
                counter = counter + 1


    # if no folder, create folder and get data.
    elif not folder:
        os.mkdir(path)
        getAllData()
    else:
        return False


'''
            get_years = []
            for i in range(0, len(YEAR)):
                if file_list[i] == YEAR[i]:
                    print(f"You have this file. {YEAR[i]}")
                else:
                    get_years.append(YEAR[i])
            print(get_years)
'''


def main():
    checkDirectory()


main()
