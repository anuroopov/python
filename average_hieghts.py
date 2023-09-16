#Average Hieght
#without using sum and len function using for loop
#---------------------------------------

#123,134,156,167,178,185,190

#using list traversal directly in FOR 

height_sum = 0
students_list = input("Enter the students hieght in cms ( separated by comma ):").split(",")
length_stud_list = len(students_list)
for i in students_list:
    #print("i is :",i)
    #print(type(i))
    height_sum = height_sum + int(i)
print("Sum of Hieghts:",height_sum )
print("Average heights:",round(height_sum/length_stud_list,2),end=" cms")

#using range function

total_sum=0
students_list = input("Enter the students hieght in cms ( separated by comma ):").split(",")
for n in range(0,len(students_list)):
    students_list[n]=int(students_list[n])
    total_sum = total_sum + students_list[n]
print("Sum of Hieghts:",total_sum )
print("Average heights:",round(total_sum/len(students_list),2),end=" cms")
    