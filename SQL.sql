
GetDate()
regular expression
https://docs.oracle.com/cd/B14117_01/appdev.101/b10795/adfns_re.htm
listunagg
https://stackoverflow.com/questions/13189575/listunagg-function
join....on...and....
rank() over (partition by..order by….desc ):rank inside group
create temporary table a select * from b
SELECT TIMESTAMP("2017-07-23")




MySQL Syntax:

SELECT column_name(s) FROM table_name WHERE condition LIMIT number;

Oracle Syntax:

SELECT column_name(s) FROM table_name WHERE ROWNUM <= number;




import cx_Oracle as ora


import pandas as pd


username ="SiyaoHu"
password = "xxxxx"
connectString="CNUDC029DF-SCAN.CNB.CORP.NET:1521/CITYACCESS_DEV"
mode=ora.SYSDBA
connection = ora.connect(username, password, connectString)

data=pd.read_sql("SELECT * FROM ETLACH.STG_ACH_TRANSACTION LIMIT 10", con=connection)
