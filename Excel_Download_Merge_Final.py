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

# set up connection to outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6).Folders("Testing")
messages = inbox.Items

# Modify the varibales based on ur search criteria 
search_subject_str = "suncorp"
search_sender_str = "anuroop"

today_date = datetime.date.today().strftime("%d-%m-%Y") 
print(today_date)
to_now = datetime.datetime.now().strftime("%d%m%Y%H%M%S") 
i=0
for msg in messages:
    i=i+1
    m_subject= str(msg.Subject).lower()
    m_sender = str(msg.Sender).lower()
    m_received_date = msg.ReceivedTime.strftime("%d-%m-%Y")    
    print(m_received_date)
    if search_subject_str in m_subject and search_sender_str in m_sender and m_received_date == today_date:
        print(m_subject + " " + str(msg.ReceivedTime))
        attachments = msg.Attachments
        attachment = attachments.Item(1)
        attachment_name = str(attachment).lower()
        attachment_name_change= attachment_name[0:-5] + "_" +str(to_now) + "_"+str(i)+'.xlsx'
        
        print(attachment_name_change) 
        attachment.SaveASFile('C:\\Users\\aov\\Desktop\\ResponsysAutomation\\ExcelMerge\\mails' + '\\' + attachment_name_change)
#-------------- Part 2 - Excel files merged -----------------#

# specifying the path to .xlsx files
path = "C:\\Users\\aov\\Desktop\\ResponsysAutomation\\ExcelMerge\\mails"
 
# csv files in the path
file_list = glob.glob(path + "/*.xlsx")
 
# list of excel files we want to merge.
# pd.read_excel(file_path) reads the 
# excel data into pandas dataframe.
excl_list = []
 
for file in file_list:
    excl_list.append(pd.read_excel(file))
 
# concatinate all DataFrames in the list, into a single DataFrame, returns new DataFrame.
excl_merged = pd.concat(excl_list, ignore_index=True)

# Empty fields - with previous row value ( optional ) 
excl_merged.fillna(method='ffill', inplace=True)

# exports the dataframe into excel file , with specified name.
excl_merged.to_excel(f'C:\\Users\\aov\\Desktop\\ResponsysAutomation\\ExcelMerge\\mails\\Suncorp_merged_{today_date}.xlsx', index=False)