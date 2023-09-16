#------------------------------------------#
# Script to download the attachments       #
# from outlook based on a search criteria  #
# and merged the files to a single file    #   
#                                          #
# -----------------------------------------#                                        
# Written By - Anuroop OV                  #
# Date : 18-08-23                          #
#------------------------------------------#

import win32com.client
import datetime
import glob
import pandas as pd
import os

#print("Suncorp- campaign analysis has started.......")
path='C:\\Users\\aov\\Desktop\\ResponsysAutomation\\ExcelMerge\\mails'
# set up connection to outlook
application = win32com.client.Dispatch('Outlook.Application')
namespace = application.GetNamespace('MAPI')
inbox_folder = namespace.GetDefaultFolder(6) 

# had to create multiple objects of subfolders to get to specific directory
inbox = inbox_folder.Folders
mobile_folder = inbox["Testing"]

# using Items method to parse specific email files within the folder
messages = mobile_folder.Items

# Modify the varibales based on ur search criteria 
search_subject_str = "suncorp"
search_sender_str = "anuroop"

today_date = datetime.date.today().strftime("%d-%m-%Y") 
#print(today_date)
to_now = datetime.datetime.now().strftime("%d%m%Y%H%M%S") 
i=0
for msg in messages:
    i=i+1
    m_subject= str(msg.Subject).lower()
    m_sender = str(msg.Sender).lower()
    m_received_date = msg.ReceivedTime.strftime("%d-%m-%Y")    
    #print(m_received_date)
    if search_subject_str in m_subject and search_sender_str in m_sender and m_received_date == today_date:
        #print(m_subject + " " + str(msg.ReceivedTime))
        attachments = msg.Attachments
        attachment = attachments.Item(1)
        attachment_name = str(attachment).lower()
        attachment_name_change= attachment_name[0:-5] + "_" +str(to_now) + "_"+str(i)+'.xlsx'
        
        #print(attachment_name_change) 
        attachment.SaveASFile(path + '\\' + attachment_name_change)
#-------------- Part 2 - Excel files merged -----------------#

# specifying the path to .xlsx files
# csv files in the path
file_list = glob.glob(path + "/*.xlsx")
 
# list of excel files we want to merge.
# pd.read_excel(file_path) reads the 
# excel data into pandas dataframe.
excl_list = []
 
for file in file_list:
   excl_list.append(pd.read_excel(file, skiprows=[0,1]))
 
# concatinate all DataFrames in the list, into a single DataFrame, returns new DataFrame.
excl_merged = pd.concat(excl_list, ignore_index=True)

# Empty fields - with previous row value ( optional ) 
excl_merged.fillna(method='ffill', inplace=True)

# exports the dataframe into excel file , with specified name.
excl_merged.to_excel(f'{path}\\Suncorp_merged_{today_date}.xlsx', index=False)

#-------------- Part 3 - Excel files Summarize -----------------#
df1 = pd.read_excel(f'{path}\\Suncorp_merged_{today_date}.xlsx')
#print(df1.Campaign.count())
df_summary = df1.groupby('Campaign').sum(numeric_only=True)
#print(df_summary)
outfile= path + "\\"+ "Suncorp__summary__"+today_date+".xlsx"
df_summary.to_excel(f'{path}\\Suncorp__summary__{today_date}.xlsx')


