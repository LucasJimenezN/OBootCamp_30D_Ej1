import pandas as pd

def getUniqueMailsFromExcel(fileName):
    readedFile = pd.read_excel(fileName)
    uniqueMails = readedFile['email'].unique()

    return uniqueMails;
