# materials:
# book(python data analysis):https://seancheney.gitbook.io/python-for-data-analysis-2nd/




import cx_Oracle as ora
import pandas as pd


username ="username"
password = "password"
connectString="server:port/servicename"
mode=ora.SYSDBA
connection = ora.connect(username, password, connectString)
data=pd.read_sql("SELECT * FROM VVIJAYAK.ACH_IN_OUT", con=connection)


Basics:
use len(df. index) for getting the number of rows, and len(df. columns) for the column count. 
df.shape[0]
df.sort_values(by='col1', ascending=False, na_position='first')
pd.DataFrame({'A' : []})
pd.DataFrame({'A' : [np.nan]})
pd.DataFrame(data, index=index, columns=columns)
df.reset_index(drop=True)

For loop:
for i in range(len(colors)):
    print(colors[i])
    
    
    
Visualization:
 https://pandas.pydata.org/pandas-docs/version/0.15.0/visualization.html
  https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.plot.html
  http://jonathansoma.com/lede/data-studio/matplotlib/adding-grid-lines-to-a-matplotlib-chart/
  
In [58]: ax = df.plot(kind='scatter', x='a', y='b',
   ....:              color='DarkBlue', label='Group 1');
   ....: 

In [59]: df.plot(kind='scatter', x='c', y='d',
   ....:         color='DarkGreen', label='Group 2', ax=ax);
  
https://stackoverflow.com/questions/40811592/pyplot-scatterdataframe-vs-dataframe-plotkind-scatter
s.startswith('Python')
s.startswith('is', 7, 10)
df.sort_values(by=['col1'])
nba["College"].fillna("No College", inplace = True)     
df[df['Team'].str.contains('Boston') & df['Position'].str.contains('PG')]     
    
my_rounded_list = [ round(elem, 2) for elem in my_list ] 
