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

#drop columns
df.drop(['B', 'C'], axis=1)


import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))



data.groupby(
    ['month', 'item']
).agg(
    {
        # Find the min, max, and sum of the duration column
        'duration': [min, max, sum],
        # find the number of network type entries
        'network_type': "count",
        # minimum, first, and number of unique dates
        'date': [min, 'first', 'nunique']
    }
    https://github.com/pandas-dev/pandas/issues/11292
    https://stackoverflow.com/questions/10373660/converting-a-pandas-groupby-output-from-series-to-dataframe

    
    fuzzy matching
    https://www.geeksforgeeks.org/fuzzywuzzy-python-library/
    https://zhuanlan.zhihu.com/p/53135935
    http://jonathansoma.com/lede/algorithms-2017/classes/fuzziness-matplotlib/fuzzing-matching-in-pandas-with-fuzzywuzzy/
    
    s1.str.contains('oG', case=True, regex=True)
    
    data.dropna()
    https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html

    
    df['year'] = pd.DatetimeIndex(df['ArrivalDate']).year
df['month'] = pd.DatetimeIndex(df['ArrivalDate']).month
    
    
    print data[['A', 'B']]
