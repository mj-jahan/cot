from zipfile import ZipFile
import os

file_set = []
name = "com_fin_xls_"
excel = "FinComYY.xls"
counter = 2017


# set file_set variable
def cleanFiles():
    for i in range(counter, 2023):
        file_set.append(f"{name}{i}.zip")


# extract from .zip
def extractFile(file):
    with ZipFile(file) as zf:
        ZipFile.extractall(zf)


# rename file
def renameFile():
    os.rename(excel, f"{counter}.xls")
    counter == counter + 1


def main():
    # create data set
    cleanFiles()
    x = 2017

    # extract all files
    for file in file_set:
        extractFile(file)
        os.rename(excel, f"{x}.xls")
        x = x + 1


if __name__ == '__main__':
    main()
