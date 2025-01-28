import pandas as pd
import zipfile as zip

directory = '/Users/marianamilhomem/Library/CloudStorage/OneDrive-Personal/Projects/Portfolio/bike-share-success-project/files/'
prefixes = ['202401', '202402', '202403', '202404', '202405', '202406', '202407', '202408', '202409', '202410', '202411', '202412']
sufix = '-divvy-tripdata.zip'

archives =[]

for i in range(len(prefixes)):
    archives.append(directory+prefixes[i]+sufix)
print(archives)

with zip.ZipFile(directory, mode='r') as myzip:
    myzip.printdir