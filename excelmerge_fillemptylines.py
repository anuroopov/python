import glob
import pandas as pd
 
# specifying the path to csv files
path = "C:\\Users\\aov\\Desktop\\ExcelMerge"
 
# csv files in the path
file_list = glob.glob(path + "/*.xlsx")
 
# list of excel files we want to merge.
# pd.read_excel(file_path) reads the 
# excel data into pandas dataframe.
excl_list = []
 
for file in file_list:
    excl_list.append(pd.read_excel(file))
 
# concatinate all DataFrames in the list
# into a single DataFrame, returns new
# DataFrame.
excl_merged = pd.concat(excl_list, ignore_index=True)
# Empty fields - with prevoius row value
excl_merged.fillna(method='ffill', inplace=True)


##duplicate removal
##excl_merged.drop_duplicates()

# exports the dataframe into excel file
# with specified name.
excl_merged.to_excel('C:\\Users\\aov\\Desktop\\ExcelMerge\\Bank_Stocks.xlsx', index=False)