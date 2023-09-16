#Paint cans calculation using a function

import math
def paint_cans(height,width,coverage):
    cans_needed = math.ceil((height * width)/coverage)
    print (f"you will need {cans_needed} paint cans:")
    
user_height = int(input("Enter the Hieght in meters :"))
user_width = int(input("Enter the Width in meters :"))
paint_cans(height=user_height,width=user_width,coverage=5)