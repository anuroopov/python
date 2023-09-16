import pandas as pd
df = pd.read_excel('C:\\Users\\aov\\Desktop\\salary.xlsx')
df = df[(df['salary'] == 300) & (df['deptno'] == 'sd0017') ]    #Filtering dataframe
df.to_excel('C:\\Users\\aov\\Desktop\\salary_filtered.xlsx', sheet_name='Filtered Data')
print(df)