# materials:
# book(python data analysis):https://seancheney.gitbook.io/python-for-data-analysis-2nd/
#https://www.geeksforgeeks.org/



import cx_Oracle as ora
import pandas as pd


username ="username"
password = "password"
connectString="server:port/servicename"
mode=ora.SYSDBA
connection = ora.connect(username, password, connectString)
data=pd.read_sql("SELECT * FROM VVIJAYAK.ACH_IN_OUT", con=connection)
https://www.geeksforgeeks.org/sql-using-python/

Basics:
use len(df. index) for getting the number of rows, and len(df. columns) for the column count. 
df.shape[0]
df.sort_values(by='col1', ascending=False, na_position='first')
pd.DataFrame({'A' : []})
pd.DataFrame({'A' : [np.nan]})
pd.DataFrame(data, index=index, columns=columns)
df.reset_index(drop=True)
list.remove('dog')

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
    })
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
    
    
    
#SYS
#Installing Python Packages from a Jupyter Notebook
#https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/    
# Install a pip package in the current Jupyter kernel
import sys
!{sys.executable} -m pip install numpy    
    
    
    

#iPython
##contain
###https://www.educative.io/edpresso/how-to-check-if-python-string-contains-another-string
##contain 
###https://www.educative.io/edpresso/how-to-check-if-python-string-contains-another-string
##measure time
###1
import time
start = time.time()
elapsed_time_fl = (time.time() - start)  #0.144280910492
###2
%%time
##substring
###https://codeigo.com/python/string-contains-a-substring
my_substring.lower() in my_string.lower()
my_string.startswith("this")
my_string.endswith("text")   
my_string.index("is")  
my_string1.count("text")
    
#object
test =  {'2', '1', '3'}
s = ', '
print(s.join(test))
str1 = “Hello”
str2 = “World”
str1 + str2    

x = ‘apples’
y = ‘lemons’
z = “In the basket are %s and %s” % (x,y)

my_string.split()[:4] # first 4 words


{0} {1} is {2} years old.” format(fname, lname, age)

music = [“Metallica”, “Rolling Stones”, “ACDC”, “Black Sabbath”, “Shinedown”]
‘ ’.join(music)
    
#List
##python maximum number of expressions in a list is 1000
##.tolist()    
>>> l=['diffuse systemic sclerosis', 'back', 'public on july 15 2008']
>>> [i.split()[0] for i in l]
##['diffuse', 'back', 'public']    
    

#DataFrame cleaning
df=df.replace('\*','',regex=True).astype(float)
pandas.Series.str.strip
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.strip.html
##split
df['AB'].str.split(' ', 1, expand=True)
data.dropna(inplace = True) 
##remove character
#https://towardsdatascience.com/5-methods-to-remove-the-from-your-data-in-python-and-the-fastest-one-281489382455
##drop rows that contain...
df[~df.Col.str.contains("XYZ")]
df[~df['your column'].isin(['list of strings'])]
s[s.str.contains('a|b'))]
>>> searchfor = ['og', 'at']
>>> s[s.str.contains('|'.join(searchfor))]
df['column'] = df['column'].fillna(value)
df.isnull().values.any()
df['acct_num'] = df['acct_num'].astype('int64')
>gapminder.rename(columns={'pop':'population',
                          'lifeExp':'life_exp',
                          'gdpPercap':'gdp_per_cap'}, 
                 inplace=True)
gapminder.rename(index={0:'zero',1:'one'}, inplace=True)
df.drop_duplicates()
df.drop_duplicates(keep='last')
df['column'] = df['column'].replace(np.nan, 0)
df[1].fillna(0, inplace=True)





#Dataframe manipulation
#list to df
pd.DataFrame(students) 
pd.DataFrame(students, columns = ['Name' , 'Age', 'City'], index=['a', 'b', 'c']) 
##merge join and concat
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
https://towardsdatascience.com/left-join-with-pandas-data-frames-in-python-c29c85089ba4
https://jakevdp.github.io/PythonDataScienceHandbook/03.07-merge-and-join.html
https://www.shanelynn.ie/merge-join-dataframes-python-pandas-index-1/

##indexing 
###https://www.geeksforgeeks.org/indexing-and-selecting-data-with-pandas/
data["Age"] #df
data[["Age", "College", "Salary"]] 
data.loc["Avery Bradley"] #series
data.loc[["Avery Bradley", "R.J. Hunter"]] #df
data.loc[["Avery Bradley", "R.J. Hunter"], 
                   ["Team", "Number", "Position"]] 
data.loc[:, ["Team", "Number", "Position"]] 
data.iloc[3]  #row  object 
data.iloc [[3, 5, 7]] 
data.iloc [[3, 4], [1, 2]] 
data.iloc [:, [1, 2]] 
data.ix["Avery Bradley"] #row object
data.ix[1] 

df.append(df2, ignore_index = True) 
df.sort_values(by=['DR_CR_CODE','TOTAL_AMOUNT'], ascending=[True, False], na_position='first')
##iteration
for index,row in df.iterrows():
    df.loc[index,'d'] = np.random.randint(0, 10)
df.set_index(['rollno','name'])
list(data_top.index) 
list(data_top.index.values) #index.values method returns an array of index.
df.stack()

data["Team"].str.split("t", n = 1, expand = True)

DataFrame.apply(self, func, axis=0, raw=False, result_type=None, args=(), **kwds)[source]
#Apply a function along an axis of the DataFrame

#advanced
##mapreduce
#https://towardsdatascience.com/a-beginners-introduction-into-mapreduce-2c912bb5e6ac
















# Data Exploration
# Import pandas package  
import pandas as pd  
    
# making data frame  
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")  

# basics
##number of item in list python
len(list)
# calling head() method   
# storing in new variable  
data_top = data.head()  

# row names
list(data.columns) 
list(data.columns.values) 
list(data.columns.values.tolist()) 
# iterating the columns 
for col in data.columns: 
    print(col) 
    
sorted(data) 

#unique values
# Create a list of unique values by turning the
# pandas column into a set
list(set(df.trucks))
list(df['trucks'].unique())

#agg
https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
##groupby sort within groups
https://stackoverflow.com/questions/27842613/pandas-groupby-sort-within-groups
df.groupby('id').head(2).reset_index(drop=True)
df.groupby('id')['value'].nlargest(2)
df.sort_values([('Group1', 'C')], ascending=False)
df.groupby(level=0).mean()
df.groupby(level="Type").mean()

