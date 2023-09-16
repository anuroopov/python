def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    days = month_days[month -1]
   
    var_lp_yr = is_leap(year)   
    if var_lp_yr == True: 
        if month == 2:
            days = days + 1
    return days
        
    
#main block   
    
var_yr= int(input("Enter a year:"))
var_month = int(input("Enter a month:"))

var_days = days_in_month(var_yr,var_month)
print ("Days in month:",  var_days )