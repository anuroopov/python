import win32com.client
import re
from datetime import date
# set up connection to outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6).Folders("Testing")
messages = inbox.Items
message = messages.GetFirst()
today_date = str(date.today())
print(today_date)
while True:
  #try:
    current_sender = str(message.Sender).lower()
    current_subject = str(message.Subject).lower()
    print(current_subject)
    # find the email from a specific sender with a specific subject
    # condition
    if re.search("suncorp - monitoring process automation",current_subject) != None and re.search("anuroop ov",current_sender) != None:
      print(current_subject) # verify the subject
      print(current_sender)  # verify the sender
      attachments = message.Attachments
      attachment = attachments.Item(1)
      attachment_name = str(attachment).lower()
      print(attachment_name) 
      attachment.SaveASFile('C:\\Users\\aov\\Desktop\\ResponsysAutomation\\ExcelMerge\\mails' + '\\' + attachment_name)
    else:
      print("inside else")
      pass
    message = messages.GetNext()
    
 # except:
 #   print("inside exeption block")
  #  message = messages.GetNext()
exit