'''
Download COT data
Extract
Ready-to-use in folder.
'''

import requests, zipfile, io, os


# single function that can be looped.
def downloadData(url, path, year, name):
    print(f"Begin {year}.xls")
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(f"{path}/")
    os.rename(f"{path}/{name}", f"{path}/{year}.xls")
    print(f"{year}.xls successful")


def getAllData():
    path = "raw_data"
    URL = "https://www.cftc.gov/files/dea/history/com_fin_xls"
    URL06_16 = 'https://www.cftc.gov/files/dea/history/fin_com_xls'
    YEAR = ['2022', '2021', '2020', '2019', '2018', '2017']
    YEAR06_16 = '2006_2016'
    name = "FinComYY.xls"
    name06_16 = "C_TFF_2006_2016.xls"

    # all years (separated)
    for year in YEAR:
        downloadData(f"{URL}_{year}.zip", path, year, name)

    # 2006-2016 (combined)
    downloadData(f"{URL06_16}_{YEAR06_16}.zip", path, YEAR06_16, name06_16)


def dialog(inDir):
    inputArg = []

    if inDir:
        print("You have directory")

        # what files in directory? should update or override directory?

    elif not inDir:
        print("[1] - Get all data and refresh directory")
        print("[2] - Enter own command line")

        choice = int(input("Enter: "))

        if choice == 1:
            getAllData()
        elif choice == 2:
            print("arguments are: str(url), str(path), str(year), str(name)")
            for i in range(0, 4):
                inputArg.append(input(f"arg[{i}]: "))


def checkDirectory():
    count = 0

    for index, file in enumerate(os.listdir()):
        if "raw_data" in file:
            count = count + 1

    if count > 0:
        dialog(True)
    elif count <= 0:
        dialog(False)




def main():
    checkDirectory()

'''
    for index, file in enumerate(os.listdir()):
        if "raw_data" in file:
            print("True")
        else:
            print("False")
'''

main()
